# Course compiler — proof of concept

**What this is:** v0 of the learning system's deterministic core — a concept
registry (`concept_registry.json`, ~25 seed entries) and a checker
(`check_concepts.py`) that verifies any unit artifact the way a compiler
verifies symbols: no concept used before the unit that introduces it;
explain-on-first-use concepts must carry their explanation where they first
appear; named-only concepts need their deferral pointer. Built 2026-07-26 in
response to Marco's ruling that MD-file rule lists do not scale (400+ entries
by unit 2, previously).

**State:** working proof. First run on Unit 1 (deck + narration + manuscript)
found 5 real violations, including the exact 60/40 case Marco flagged, and
showed the manuscript's 60/40 explanation had been lost at storyboard
compression. Design rationale and the full three-machine system:
`qsl-product/EBI Production/learning-system-design.md`.

**What it becomes:** if Marco approves the design — full registry seeded from
the 27-unit syllabus, the checker wired into workflow steps 4 and 6, and a
capture path where each Marco correction lands as one registry entry / lint
pattern / eval case. Promotion target open (qsl-ebi tools vs qsl-product vs
qsl-infra — Marco's call).

**Run:** `python3 check_concepts.py --unit 1 <files in student-facing order>`

**Extended 2026-07-26 (same day):** the generic layer answering Marco's
"50–60 little teaching moments" question — `rule_cards.json` (one store,
every correction one card with a scope) + `check_rules.py` (generic runner:
three assertion types execute all lint cards; reviewer cards are retrieved
by scope in the model pass; template cards are enforced by the scaffold
itself). Routing priority: template > lint > reviewer. First run: Unit 1
deck passes the 4 seeded presentation cards. The concept registry is a
special case of this store with a dedicated checker.
