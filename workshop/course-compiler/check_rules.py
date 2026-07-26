#!/usr/bin/env python3
"""Generic rule-card runner v0 (proof of concept).

Executes every card in rule_cards.json whose enforce == "lint" against a
deck HTML file. Three generic assertion types cover most presentation
conventions; a new convention is a new CARD, not new code:

  per_slide_required  every <section class="slide"> must contain pattern
  slide_if_then       any slide containing IF must also contain THEN
  regex_forbidden     pattern must not appear anywhere

Cards with enforce == "reviewer" are listed (they feed the scoped model
review pass, retrieved by scope). Cards with enforce == "template" are
listed for the record - their enforcement is the template itself.

Usage: python3 check_rules.py deck.html
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLIDE_SPLIT = re.compile(r'<section class="slide[^"]*">')


def main():
    deck_path = sys.argv[1]
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
          f"{len(reviewer)} reviewer cards (scoped retrieval) · {len(template)} template cards (enforced by scaffold)")
    if failures:
        print(f"\n{len(failures)} FAILURE(S):")
        for cid, msg in failures:
            print(f"  [{cid}] {msg}")
        return 1
    print("lint: all pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
