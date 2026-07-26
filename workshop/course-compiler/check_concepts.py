#!/usr/bin/env python3
"""Course compiler v0 (proof of concept) — concept-dependency checker.

Reads the concept registry and checks one unit's artifacts the way a
compiler checks symbols: a concept may not be used before the unit that
introduces it; a concept marked explain_on_first_use must carry its
first-use explanation in the artifact where it first appears; named_only
concepts may be named but, where required, must sit near a deferral
phrase ("later units show...").

Usage: python3 check_concepts.py --unit 1 file1.html file2.md ...
Exit code 1 if any violation. Findings name file, line, concept, rule.

This is deliberately dumb and deterministic: alias matching with word
boundaries, HTML tags stripped. A model reviewer pass for semantic
leakage sits on top of this in the full design; this layer alone already
catches the class of error that prompted it (60/40 used, never declared).
"""
import argparse, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TAG = re.compile(r"<[^>]+>")
DEFER_WINDOW = 400  # chars around a named_only hit in which a deferral phrase must appear


def load_registry():
    return json.loads((HERE / "concept_registry.json").read_text())["concepts"]


def strip_html(text):
    return TAG.sub(" ", text)


def find_hits(text, alias):
    a = alias.strip()
    if alias.startswith(" ") or alias.endswith(" "):        # explicit-boundary alias
        pat = re.compile(re.escape(alias), re.I)
    else:
        pat = re.compile(r"(?<![\w/])" + re.escape(a) + r"(?![\w])", re.I)
    return [m.start() for m in pat.finditer(text)]


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def check_file(path, unit, registry, first_use_seen):
    raw = Path(path).read_text()
    text = strip_html(raw) if path.endswith((".html", ".htm")) else raw
    findings = []
    for c in registry:
        hits = []
        for alias in c["aliases"]:
            hits += [(p, alias) for p in find_hits(text, alias)]
        if not hits:
            continue
        hits.sort()
        pol, intro = c["policy"], c.get("introduced_in")
        if pol == "assumed_known":
            continue
        if pol == "full_unit" and intro and unit < intro:
            p, al = hits[0]
            findings.append((path, line_of(text, p), c["id"],
                             f"USED BEFORE INTRODUCED — '{al}' belongs to unit {intro}; this is unit {unit}"))
            continue
        if pol == "named_only":
            if intro and unit >= intro:
                continue
            if c.get("named_only_requires_deferral"):
                ok = any(ph.lower() in text.lower() for ph in c["deferral_phrases"])
                if not ok:
                    p, al = hits[0]
                    findings.append((path, line_of(text, p), c["id"],
                                     f"NAMED WITHOUT DEFERRAL — '{al}' may be named before unit {intro} only next to a pointer like 'Unit 3 shows how such numbers are measured'"))
            continue
        if pol == "explain_on_first_use":
            if intro and unit < intro:
                p, al = hits[0]
                findings.append((path, line_of(text, p), c["id"],
                                 f"USED BEFORE INTRODUCED — '{al}' is introduced in unit {intro}"))
                continue
            if c["id"] in first_use_seen:
                continue
            p, al = hits[0]
            req = c.get("spoken_must_contain") if path.endswith("narration.md") and c.get("spoken_must_contain") else c.get("first_use_must_contain", [])
            window = text[p:p + 600]
            if all(phrase.lower() in window.lower() for phrase in req):
                first_use_seen.add(c["id"])
            else:
                findings.append((path, line_of(text, p), c["id"],
                                 f"FIRST USE UNEXPLAINED — '{al}' must carry its explanation at first use (required: {req})"))
                first_use_seen.add(c["id"])  # report once per run
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--unit", type=int, required=True)
    ap.add_argument("files", nargs="+")
    args = ap.parse_args()
    registry = load_registry()
    first_use_seen = set()
    all_findings = []
    for f in args.files:          # order matters: pass files in student-facing order
        all_findings += check_file(f, args.unit, registry, first_use_seen)
    if not all_findings:
        print(f"OK — unit {args.unit}: no concept violations in {len(args.files)} file(s)")
        return 0
    print(f"UNIT {args.unit}: {len(all_findings)} concept violation(s)\n")
    for path, line, cid, msg in all_findings:
        print(f"  {Path(path).name}:{line}  [{cid}]  {msg}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
