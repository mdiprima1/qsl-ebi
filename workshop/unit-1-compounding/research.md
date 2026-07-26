# Unit 1 research file — Compounding

**Workflow step 2 of 6.** Deliberately over-collected: more than the unit will use. The manuscript draws from this file; nothing enters a slide that is not traceable to a source or to `compute_unit1.py`.

## 1. The core mechanism (internal, computed)

- Growth on growth: $100,000 at 7.7% earns $7,700 in year 1; year 10 earns $15,012; year 30 earns $66,183 — the rate never changes, the balance it lands on does. (CSV: `grow_*`.)
- 40-year lump sum: $100,000 at 7.7% → $1,950,000. (CSV: `lump100k_40y_77`.)
- Two-savers case: $300/month at 7.7%, start 25 vs 35 → $890,000 vs $400,000 at 65; deposits $144,000 vs $108,000. The late saver deposits 25% less and ends 55% behind (2.23×). (CSV: `saver_*`, `end_gap_ratio`.)
- Cost of one year of delay: start at 26 instead of 25 → $67,000 less at 65, against $3,600 not deposited that year. (CSV: `delay_1y_cost`.)
- Catch-up cost: matching the 25-starter from 35 requires $670/month vs $300 — more than double, for thirty years. (CSV: `catchup_monthly_from_35`.)
- Rate × years: $500/month, 40 years → $365,000 at 2.0% · $1,500,000 at 7.7% · $2,700,000 at 9.9%. (CSV: `t500_*`.)

## 2. The three life scenarios (old deck, recomputed)

Same calculator both directions: accumulation to a pot, then the level monthly payout to age 95 leaving a fifth of the pot (RESERVE 0.2). All in CSV (`maya_*`, `daniel_*`, `rosa_*`):

| | 2.0% | 7.7% | 9.9% |
|---|---|---|---|
| Maya, 22, $0 + $300/mo, payouts 65 | $245,000 → $800/mo | $1,150,000 → $7,650/mo | $2,150,000 → $18,000/mo |
| Daniel, 40, $50k + $1,000/mo, payouts 60 | $370,000 → $1,100/mo | $770,000 → $5,100/mo | $1,050,000 → $8,450/mo |
| Rosa, 65, $1,000,000, payouts now | → $3,400/mo | → $7,400/mo | → $9,150/mo |

Teaching value: three life stages, one formula; Rosa shows the return keeps deciding the outcome after saving ends.

## 3. Rates and their provenance

- 2.0% savings account (stylized) · 7.7% = 60/40 portfolio average annual return, 2005–2026 · 9.9% = S&P 500, 2005–2026. Carried from the old free-course Unit 1 deck (`qsl-hq/blueprint/COURSE-FREE/unit-1/build_unit1.py`), which computed them from QSL backtests. Unit 3 teaches how such numbers are measured.
- **The menu of five real rates (Marco directive 2026-07-26 — the unit's demonstration set):** The Defender 6.2%/yr (2015–2026) · 60/40 portfolio 7.7%/yr (2005–2026) · SPY buy-and-hold 7.9%/yr full history (1998–2026) · The Diversifier 14.1%/yr (2015–2026) · The Growth Engine 41.8%/yr (2015–2026). Strategy numbers from `qsl-research/demo-strategies/overview-table.md` (QC-native); 60/40 from the old-deck backtest. Doubling times (rule of 72): 11.6y · 9.4y · 9.1y · 5.1y · 1.7y. (CSV: `menu_*`, `double_*`.)
- Window honesty per `CHAPTER-1-REFERENCE.md`: 2015–2026 is a strong bull that flatters the Growth Engine and understates the Defender; SPY full-history carries the true −49% drawdown era. In this unit the caveat is a hint, not a lesson (risk arrives in later units).
- Open item: Marco asked for the **long-term** 60/40 number; the recorded QSL figure is 7.7% over 2005–2026. A full-history 60/40 backtest (e.g. 1998–2026 to match SPY) does not exist in the vault yet — a QRES ticket if wanted.

## 3a. Catching up by rate (computed — the unit's second key table)

The annual return that makes $300/month from a later start match the 25-starter's $890,000 at 65 (CSV: `catchup_rate_from_*`):

| Start | Years | Required return | Where it sits on the menu |
|---|---|---|---|
| 25 | 40 | 7.7% | the conservative rows |
| 35 | 30 | 11.9% | below The Diversifier's 14.1% |
| 40 | 25 | 15.5% | just above The Diversifier |
| 45 | 20 | 21.6% | between Diversifier and Growth Engine |

Teaching value: every required rate sits inside the span real strategies delivered. Late starts are recoverable via the rate lever; the cost of the higher rate is hinted, taught later.

## 4. Why intuition fails (external, cited)

- **Exponential growth bias** — the tendency to linearize exponential functions when assessing them intuitively. Households underestimate future values given investment terms; more-biased households borrow more, save less, favor shorter maturities. [Stango & Zinman, "Exponential Growth Bias and Household Finance," *Journal of Finance*, 2009](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2009.01518.x) ([SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1081633)).
- Follow-on literature: bias leads people to start saving too late ([Levy & Tasoff, exponential-growth bias and lifecycle consumption](https://personal.lse.ac.uk/levymr/papers/LevyTasoff.pdf)); framing savings goals as future values vs contributions changes behavior ([McKenzie & Liersch](https://pages.ucsd.edu/~mckenzie/McKenzie%26LierschInPressJMR.pdf)).
- Teaching implication: the unit should let the student *feel* the underestimate (commit to a guess before the reveal), not merely assert the bias.

## 5. Compounding against the saver (computed + cited)

- A 1% annual fee at a 7.7% gross return, 40 years, $100,000: $1,950,000 → $1,350,000. The fee consumes ~31% of the no-fee ending — the fee is 1%, the damage is 31×. (CSV: `lump100k_40y_67net`, `fee1pct_40y_lost`.)
- Regulator's framing of the same effect: [SEC Investor Bulletin — How Fees and Expenses Affect Your Portfolio](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/updated); [investor.gov, Understanding Fees](https://www.investor.gov/introduction-investing/getting-started/understanding-fees).
- Same arithmetic runs on debt (interest compounds against the borrower) — mention, defer detail.

## 6. The rule of 72 (computed)

Doubling time ≈ 72 / rate-in-percent. Accuracy at our three rates: 2.0% → rule 36.0y vs exact 35.0y · 7.7% → 9.4y vs 9.3y · 9.9% → 7.3y vs 7.3y. Good enough for mental checks across the course. (CSV: `double_exact_*`, `double_rule72_*`.)

## 7. Collected but NOT used (and why)

- Einstein "eighth wonder of the world" quote — apocryphal; also aphorism (banned register).
- Chessboard/rice doubling parable — cliché; replaced by the student's own guess on the two-savers chart.
- Specific inflation-adjusted (real) return figures — need an inflation series with provenance; inflation is deferred by syllabus scope. Named qualitatively only.
- Buffett's snowball biography material — personality-driven; the course teaches the arithmetic, not the person.
- Daily-vs-annual compounding frequency detail — real distinction, but a digression at unit 1 depth; the simulator compounds monthly, noted there.

## 8. Assets for production (step 5, later)

Two-savers curve (chart_points.txt) · single-year earnings bars ($7,700 → $66,183) · rate × years three-bar comparison · fee-drag paired bars · the scenario table · simulator screenshot/link (`/compound`).
