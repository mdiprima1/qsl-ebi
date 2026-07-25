# Course modules — the structured content library

This folder holds the teaching content of the QSL course **Evidence-Based Investing for Everyone**, organized as self-contained modules: one folder per concept, everything that concept needs inside it. Modules are assembled into course units later — a unit is a selection of modules plus connective narration. Modules never move once filed; units reference them.

New material is not created here. It is created in `../workshop/` (the work-in-progress space) and **promoted** here when it is mature. Read `../workshop/README.md` for that workflow.

## Layout

```
modules/
  ch1-return-and-risk/       one folder per course chapter,
  ch2-backtesting/           mirroring the course syllabus
  ch3-strategy-families/
  ch4-validation/
  ch5-operating/
  _unassigned/               mature modules with no chapter decision yet
```

Each module:

```
ch1-return-and-risk/
  volatility/
    README.md        the manifest (see below)
    slides/          the HTML slide sequence + rendered PNGs
    data/            the data files every number on the slides comes from
    narration.md     the spoken script, per slide
```

## The module manifest (`README.md`, ~10 lines)

Every module carries one. It is the entire tracking system:

```markdown
# Volatility
- chapter: ch1-return-and-risk
- template slides present: Scenario, Definition, Worked example   (of the five)
- data: AAPL/TSLA daily closes May 2026 (data/…csv); SPY 2021–2025 (data/…csv)
- status: draft | review | approved | in-unit
- history: 2026-07-25 promoted from workshop/volatility-sequence (draft)
```

## The concept-introduction template (the five slides)

Every module that introduces a new concept follows this fixed sequence:

1. **Scenario** — a concrete market situation with named assets and a stated period, built on a genuine contrast or decision problem. It ends on a question the student answers before anything is taught; the reveal belongs to the next slide. Never open with theory or a formula.
2. **Intuition** — starts by engaging the obvious naive answer to the Scenario question (what a sensible beginner would try, and precisely where it falls short), then gives the core idea in plain English. No notation unless unavoidable.
3. **Definition** — the formal term, a plain-English definition, then the simplest correct formula, shown briefly, every symbol named in words. No derivations. A concept with no meaningful one-line formula carries the definition without one.
4. **Worked example** — the same formula walked through real data, inputs to conclusion, with simple numbers. The example proves what the student can now do; it does not restate the definition.
5. **Considerations** — assumptions, edge cases, and the conditions under which the concept misleads, stated honestly. Forward-looking: each consideration seeds a later unit. The spoken close ends with one short check question.

Optional, non-default: a **Procedure** slide after slide 4, only for concepts that are inherently process-driven (Monte Carlo simulation, bootstrapping, optimization).

The step names above are internal. On-slide titles are concept-specific and state the concrete thing ("Two stocks, one return"), never the category ("Scenario").

## Content rules (binding for every module)

- **Every number comes from a data file in the module's `data/` folder.** No number appears on a slide or in narration that cannot be traced to a file. Invented data is never acceptable.
- Every number has a named asset and a stated period.
- Prose is written for a beginner with no statistics or programming background: short sentences, one idea each, plain words. Necessary jargon is explained on first use; unnecessary jargon is replaced.
- No exclamation marks. Never "retail trader" — say "individual investor" or "independent investor."

## Status lifecycle

`draft` → `review` (awaiting approval) → `approved` → `in-unit` (assembled into a live course unit). Only the course owner moves a module to `approved`. The manifest records every transition with a date.

## Module index

| Module | Chapter | Status |
|---|---|---|
| *(none yet — first candidates are maturing in `../workshop/`)* | | |

Keep this table current: one line per module, updated in the same commit that changes a module's status.
