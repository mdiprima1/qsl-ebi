# Workshop — the work-in-progress space

This folder is where course material gets **created**. It is deliberately unstructured: an AI team can be pointed here and simply build — slide experiments, brainstorms, half-formed sequences, visual ideas. Nothing in this folder is part of the course. The course lives in `../modules/`; material gets there through promotion (below).

## The workflow this folder exists for

1. **Build here, freely.** Start slides for a concept, try a visual approach, draft a sequence. Order and completeness are not required.
2. **Promote later.** When a piece matures, it is promoted into `../modules/<chapter>/<concept>/`, gains a module manifest, and enters the status lifecycle. Promotion is an explicit step, done deliberately — never assume workshop material is course-approved.
3. After promotion, the workshop copy is deleted, or its `NOTE.md` is marked `promoted → modules/<path>` if the folder still holds unpromoted material.

## The three rules (everything else is open)

Only three rules apply here. They exist so that nothing built in this folder is ever wasted:

1. **One folder per piece of work**, named plainly (`volatility-sequence/`, `drawdown-chart-ideas/`). No loose files at the top level.
2. **Every folder carries a `NOTE.md`** — a few lines: what this is, what state it is in, what it might become. An agent finding the folder cold must understand it from the note alone.
3. **Every number comes from a data file in the folder.** This is the one content rule that binds even in draft, because a slide with untraceable numbers can never be promoted. Named assets, stated periods, real data.

Categories: none imposed. Create folders as the work suggests them. If a natural grouping emerges (e.g., several chart experiments), group them; do not build a taxonomy up front.

## What this folder is not

- Not the course. Students never see this folder's content through the platform.
- Not the strategy zone. `../strategies/` runs under `../PACKAGE-SPEC.md` integrity rules; workshop work never touches it.
- Not private. This repository is public — push work here when it is fit to be seen. Material that should stay private matures elsewhere first.

## Target shape for slide work

Slide work here should aim at the five-slide concept template described in `../modules/README.md` (Scenario → Intuition → Definition → Worked example → Considerations). Partial coverage is fine — that is what the workshop is for — but knowing the target shape saves rework at promotion.
