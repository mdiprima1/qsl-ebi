#!/usr/bin/env python3
"""Generic rule-card runner v0 (proof of concept).

Executes every card in rule_cards.json whose enforce == "lint" against a
deck HTML file. Three generic assertion types cover most presentation
conventions; a new convention is a new CARD, not new code:

  per_slide_required  every <section class="slide"> must contain pattern
  slide_if_then       any slide containing IF must also contain THEN
  regex_forbidden     pattern must not appear anywhere

Cards with enforce == "reviewer" run as LLM calls when --reviewer is
passed: cards are batched BY SCOPE, each batch gets one model call with a
bounded prompt (that scope's cards + the matching artifact slice only),
and the model must return JSON verdicts quoting the offending line for
every failure - quotes make verdicts verifiable. Transport: the `claude`
CLI (MAX subscription), same as the voice engine. Cards with enforce ==
"template" are listed for the record - the scaffold enforces them.

Usage: python3 check_rules.py deck.html [--reviewer]
"""
import json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLIDE_SPLIT = re.compile(r'<section class="slide[^"]*">')


def slice_for_scope(html, slides, scope):
    """The bounded artifact slice a reviewer batch sees. New scope -> add an
    extractor here once; every future card in that scope reuses it."""
    if scope == "slide":
        titles = re.findall(r"<h1>(.*?)</h1>", html, re.S)
        return "Slide titles, in order:\n" + "\n".join(
            f"{i:02d}. {re.sub('<[^>]+>', '', t).strip()}" for i, t in enumerate(titles, 1))
    if scope == "table":
        tables = re.findall(r"<table.*?</table>", html, re.S)
        return "\n\n".join(re.sub(r"<[^>]+>", " ", t) for t in tables) or "(no tables)"
    if scope == "chart":
        keep = [f"SLIDE {i:02d}:\n" + re.sub(r"<(svg|polyline|rect|line|text)[^>]*>|</svg>", " ",
                re.sub(r"<[^>]+>", " ", s))[:1500]
                for i, s in enumerate(slides, 1) if "<svg" in s or 'class="bars"' in s]
        return "\n\n".join(keep) or "(no charts)"
    return re.sub(r"<[^>]+>", " ", html)[:8000]


def run_reviewer_batch(scope, cards, artifact_slice):
    card_text = "\n".join(
        f"- [{c['id']}] {c['rule']}" +
        (f"\n  good: {c['good_example']}" if c.get("good_example") else "") +
        (f"\n  bad: {c['bad_example']}" if c.get("bad_example") else "")
        for c in cards)
    prompt = f"""You are a review gate for course slides. Judge the artifact below ONLY against these rule cards — no other opinions, no style preferences of your own.

RULE CARDS (scope: {scope}):
{card_text}

ARTIFACT:
{artifact_slice}

Return ONLY a JSON array, one object per card:
[{{"card_id": "...", "verdict": "PASS" or "FAIL", "failures": [{{"location": "slide/table ref", "quote": "the exact offending text", "why": "one sentence"}}]}}]
A FAIL without a verbatim quote from the artifact is invalid — omit it."""
    r = subprocess.run(["claude", "-p", prompt], capture_output=True, text=True, timeout=300)
    out = r.stdout.strip()
    m = re.search(r"\[.*\]", out, re.S)
    if not m:
        return [{"card_id": c["id"], "verdict": "ERROR", "failures": [],
                 "raw": out[:200] or r.stderr[:200]} for c in cards]
    return json.loads(m.group(0))


def main():
    deck_path = sys.argv[1]
    use_reviewer = "--reviewer" in sys.argv
    html = Path(deck_path).read_text()
    slides = SLIDE_SPLIT.split(html)[1:]
    cards = json.loads((HERE / "rule_cards.json").read_text())["cards"]
    failures, reviewer, template = [], [], []
    for c in cards:
        if c["enforce"] == "reviewer":
            reviewer.append(c); continue
        if c["enforce"] == "template":
            template.append(c); continue
        chk = c["check"]
        if chk["type"] == "per_slide_required":
            for i, s in enumerate(slides, 1):
                if chk["pattern"] not in s:
                    failures.append((c["id"], f"slide {i:02d}: missing '{chk['pattern']}' — {c['rule']}"))
        elif chk["type"] == "slide_if_then":
            for i, s in enumerate(slides, 1):
                if chk["if"] in s and chk["then"] not in s:
                    failures.append((c["id"], f"slide {i:02d}: has '{chk['if']}' but no '{chk['then']}' — {c['rule']}"))
        elif chk["type"] == "regex_forbidden":
            for m in re.finditer(chk["pattern"], html):
                failures.append((c["id"], f"forbidden pattern at char {m.start()} — {c['rule']}"))
    lint_count = len(cards) - len(reviewer) - len(template)
    print(f"{Path(deck_path).name}: {len(slides)} slides · {lint_count} lint cards run · "
          f"{len(reviewer)} reviewer cards · {len(template)} template cards (enforced by scaffold)")
    if failures:
        print(f"\n{len(failures)} LINT FAILURE(S):")
        for cid, msg in failures:
            print(f"  [{cid}] {msg}")
    else:
        print("lint: all pass")
    reviewer_failed = False
    if use_reviewer and reviewer:
        by_scope = {}
        for c in reviewer:
            by_scope.setdefault(c["scope"], []).append(c)
        for scope, batch in by_scope.items():
            print(f"\nreviewer [{scope}]: {len(batch)} card(s), one model call...")
            for v in run_reviewer_batch(scope, batch, slice_for_scope(html, slides, scope)):
                if v["verdict"] == "PASS":
                    print(f"  [{v['card_id']}] PASS")
                elif v["verdict"] == "ERROR":
                    print(f"  [{v['card_id']}] ERROR — {v.get('raw','')}"); reviewer_failed = True
                else:
                    reviewer_failed = True
                    print(f"  [{v['card_id']}] FAIL")
                    for f in v.get("failures", []):
                        print(f"      {f.get('location','?')}: \"{f.get('quote','')[:90]}\" — {f.get('why','')}")
    return 1 if (failures or reviewer_failed) else 0


if __name__ == "__main__":
    sys.exit(main())
