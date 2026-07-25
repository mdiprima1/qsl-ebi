# Volatility slide sequence — work in progress

**What this is:** the volatility concept introduction, retrofitted 2026-07-25 to the full five-slide template — (1) Scenario: AAPL vs TSLA, May 2026, both +11.5%, ends on the committed question; (2) Intuition: worst-day answer engaged (−4.75% vs −1.18%), typical daily move 2.1% vs 0.9%; (3) Definition: volatility, standard deviation, the formula with symbols named; (4) Worked example: daily-return bars, 0.94% vs 2.49%, ratio stated as more than two and a half times (2.65 computed); (5) Considerations: both directions, time scales (√252), measured-period caveat, shape-of-moves seed. Open `volatility_sequence.html` in a browser. Narration per slide in `narration.md`, each block ending with a spoken summary; the closing check question ends slide 5's block.

**State:** draft — template-complete, awaiting Marco's slide-by-slide review. Every number verified against `data_202605_aapl_tsla.csv` (totals 11.50%/11.51%, typical move 0.86%/2.11% shown rounded, SD 0.94%/2.49%, worst days −1.18%/−4.75%). The earlier version's SPY 2021–2025 time-scales slide was replaced by a qualitative Considerations point, so the missing SPY data file is no longer a blocker. `data_2016_gld_lqd.csv` is an earlier example, kept for reference.

**Open flag (carried from the pilot):** slide 2 uses the plain "typical daily move" (mean absolute move, 2.1%/0.9%) and slides 3–4 the standard deviation (2.49%/0.94%) — plain-first-then-formal by design; Marco to confirm or collapse to one statistic.

**What it becomes:** `modules/ch1-return-and-risk/volatility/` after approval.

**History:** 2026-07-24 three-slide pilot (QSL VOICE engine) · 2026-07-25 imported to workshop · 2026-07-25 retrofitted to the five-slide template.
