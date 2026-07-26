# Unit 1 brief — Compounding

**Syllabus row:** Unit 1, Chapter 1 — "Compounding — The superpower many forget."
**Length target:** 30–45 minutes. **Workflow step 1 of 6** (`qsl-product/EBI Production/course-authoring-workflow.md`).

## The unit's key message (Marco, 2026-07-26)

Time and rate are interchangeable levers. Started early, conservative compounding rates (the 6–8% end of the menu) produce great results. Started later, a higher compounding rate can reach the same destination — and the menu of five real, measured returns (roughly 6% to 40%) shows such rates have been delivered by disciplined methods. The cost of higher rates (risk, volatility) belongs to later units: **hint, do not highlight** — a faster-compounding strategy asks more of the investor holding it. The unit ends constructive: a student who feels behind should leave knowing the catch-up path is real and this course teaches the skill it requires.

## What the student can do after this unit

1. Compute an ending value from a starting amount, an annual return, and a number of years — by hand with FV = P × (1 + r)ⁿ, and with the QSL simulator.
2. Explain why ending values grow faster than deposits, and why the starting year matters more than the deposit total.
3. Estimate a doubling time in their head with the rule of 72, and say how accurate it is.
4. Quantify what an annual fee costs over decades, and explain why the cost is several times the fee.
5. Run the same arithmetic in the other direction: from a saved sum to the monthly amount it can pay out.
6. State why a steady rate is an average, not a promise — and name the question that raises about any return number.
7. Compute the annual rate a later start requires to match an early start, and locate that rate on the menu of real strategy returns.

## The quiz questions (written first, per backward design)

1. Two savers invest $300 a month at the same return. One starts at 25, one at 35. The late starter deposited 25% less. At 65 he has: (a) about 25% less · (b) about 40% less · **(c) less than half** · (d) about the same.
2. A fund charges a 1% annual fee. Over 40 years at 7.7%, roughly what share of the no-fee ending value does the fee consume? (a) 1% · (b) 4% · (c) 10% · **(d) about 30%**.
3. At 9.9% a year, money doubles in about: (a) 10 years · **(b) 7 years** · (c) 14 years · (d) 4 years. (Rule of 72.)
4. To finish at 65 with what a $300-a-month saver starting at 25 reaches, someone starting at 35 must save about: (a) $370 · (b) $450 · **(c) $670** · (d) $900 a month.
5. Rosa retires at 65 with $1,000,000. Why does the same million pay $2,500 a month in one case and $7,400 in another? **The return keeps working during the payout years; the rate decides how fast the pot refills as it drains.**
6. Saving $300 a month from age 35, roughly what annual return matches a 25-starter earning 7.7% by age 65? (a) 8.5% · **(b) about 12%** · (c) about 25% · (d) no rate can close the gap.

## The misconceptions this unit must break

- **Linear thinking.** Twice the deposits ≈ twice the ending; twice the years ≈ twice the money. (Both wrong; the second badly. Documented as exponential growth bias — people linearize growth, and more-biased households save less. Stango & Zinman, *Journal of Finance*, 2009.)
- **Small differences are small.** One or two percentage points of return, or a 1% fee, feel negligible; over decades they separate outcomes by hundreds of thousands of dollars.
- **A late start is cheap to fix.** With money as the only lever, matching a ten-years-earlier start costs more than double the monthly saving, for thirty years. (The unit then reopens the door with the second lever: the rate.)
- **A late start cannot be fixed.** The opposite error, and the one this unit must end by breaking: the required catch-up rates (about 12% from 35, about 22% from 45) sit inside the range real strategies have delivered.
- **The steady rate is real.** No market pays the same rate every year; 7.7% is an average over a stated window.
- **After retirement the return stops mattering.** The payout side runs on the same formula.

## Scope

**In:** the compounding mechanism · FV = P × (1 + r)ⁿ · rate × years · the three life scenarios (accumulate and pay out) · fees as compounding against the saver · the rule of 72 · the course strategies' real average returns as a first, partial view (windows stated) · the simulator.
**Out (deferred, named where relevant):** how return numbers are measured (Unit 3) · risk and the variation around the average (Unit 4 on) · inflation and tax mechanics (later units) · any strategy detail (Chapters 2–3).

## Anchor use (syllabus design principle 1)

First partial view of the three certified strategies, presented as a **five-row menu of real rates** together with long-term SPY and the 60/40 portfolio: The Defender 6.2% · 60/40 7.7% (2005–2026) · SPY 7.9% (full history 1998–2026) · The Diversifier 14.1% · The Growth Engine 41.8% (strategy windows 2015–2026). Averages and doubling times only, windows stated, explicitly marked as partial — full treatment arrives in Chapters 2–4.

## Numbers

Every figure in the unit is generated by `compute_unit1.py` into `data_unit1_compounding.csv`, or cited from `qsl-research/demo-strategies/overview-table.md` (the QC-native Chapter-1 reference).
