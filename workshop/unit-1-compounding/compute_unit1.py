#!/usr/bin/env python3
"""Unit 1 (Compounding) — data generator for the workshop draft.

Reproduces the calculator from the old free-course Unit 1 deck
(qsl-hq/blueprint/COURSE-FREE/unit-1/build_unit1.py) so every number
shown on the slides traces to this file's output.

Outputs:
  data_unit1_compounding.csv   every figure used on the slides
  chart_points.txt             SVG polyline coordinates for the slide-1 chart

Rates (inputs, every one real and sourced per rule card numbers-real-market):
  0.38% savings account — FDIC national average savings rate, July 2026
        (fdic.gov national rates; replaced the old stylized 2.0%)
  7.7%  60/40 portfolio average annual return, 2005-2026 (QSL backtest)
  9.9%  S&P 500 average annual return, 2005-2026 (QSL backtest)
"""
import csv, datetime, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
R2, R64, RSP = 0.0038, 0.077, 0.099  # R2 = FDIC national average savings, Jul 2026
RESERVE = 0.2  # fifth of the pot still remaining at the end of payouts


def pot_and_safe(capital, monthly, age, draw_age, rate, end_age=95):
    """End value at draw_age, and the level monthly payout to end_age
    that leaves RESERVE of the pot remaining (old deck formula)."""
    rm = (1 + rate) ** (1 / 12) - 1
    n_grow = (draw_age - age) * 12
    n_draw = (end_age - draw_age) * 12
    g = (1 + rm) ** n_grow
    pot = capital * g + monthly * ((g - 1) / rm)
    gn = (1 + rm) ** n_draw
    safe = (pot * gn - RESERVE * pot) * rm / (gn - 1)
    return pot, safe


def rk(x):  # display rounding, same steps as the old deck
    if x >= 1_000_000: return round(x / 50_000) * 50_000
    if x >= 100_000: return round(x / 5_000) * 5_000
    if x >= 10_000: return round(x / 500) * 500
    return round(x / 50) * 50


def balances(monthly, years, rate):
    """Month-end balances for a monthly saver, year granularity out."""
    rm = (1 + rate) ** (1 / 12) - 1
    bal, out = 0.0, []
    for m in range(1, years * 12 + 1):
        bal = bal * (1 + rm) + monthly
        if m % 12 == 0:
            out.append(bal)
    return out


rows = []

def rec(name, value, display, note):
    rows.append({"name": name, "value": round(value, 2), "display": display, "note": note})


# --- Slide 1/2: two savers, $300/month at 7.7%, start 25 vs 35, read at 65 ---
potA, _ = pot_and_safe(0, 300, 25, 65, R64)
potB, _ = pot_and_safe(0, 300, 35, 65, R64)
contribA, contribB = 300 * 12 * 40, 300 * 12 * 30
rec("saver_early_end_65", potA, f"${rk(potA):,.0f}", "$300/mo at 7.7%, age 25 to 65 (40y)")
rec("saver_late_end_65", potB, f"${rk(potB):,.0f}", "$300/mo at 7.7%, age 35 to 65 (30y)")
rec("saver_early_contrib", contribA, f"${contribA:,.0f}", "total deposits, 480 months")
rec("saver_late_contrib", contribB, f"${contribB:,.0f}", "total deposits, 360 months")
rec("contrib_gap_pct", (contribA - contribB) / contribA * 100, "25%", "late saver deposited 25% less")
rec("contrib_ratio", contribA / contribB, f"{contribA / contribB:.2f}x", "early deposits / late deposits (a third more)")
rec("end_gap_ratio", potA / potB, f"{potA / potB:.2f}x", "early ending / late ending")

# --- Slide 3: one step of the formula ---
rec("formula_step_100k", 100_000 * (1 + R64), "$107,700", "$100,000 x 1.077, one year")

# --- Slide 4: $100,000 at 7.7%, growth earning growth (old deck slide 2) ---
for label, yr in (("y1", 1), ("y2", 2), ("y3", 3), ("y10", 10), ("y30", 30)):
    start = 100_000 * (1 + R64) ** (yr - 1)
    earned = start * R64
    rec(f"grow_{label}_start", start, f"${start:,.0f}", f"balance entering year {yr}")
    rec(f"grow_{label}_earned", earned, f"${earned:,.0f}", f"earned during year {yr} at 7.7%")

# --- Slide 5: rate x years — $500/month, 40 years, three rates (old deck slide 3) ---
for r, label, note in ((R2, "rate2", "0.38% savings account (FDIC national average, Jul 2026)"),
                       (R64, "rate77", "7.7% 60/40 portfolio 2005-2026"),
                       (RSP, "rate99", "9.9% S&P 500 2005-2026")):
    pot = pot_and_safe(0, 500, 25, 65, r)[0]
    rec(f"t500_{label}", pot, f"${rk(pot):,.0f}", f"$500/mo, 40y at {note}")

# --- The real path: $100,000 in the 60/40, Jan 2015 - Jun 2026 -------------
# Source: data_6040_2015_2026_qc.json (QC-native backtest, copied from
# qsl-research/demo-strategies/BENCHMARKS/results). Real year-by-year path
# per rule card numbers-real-market (Marco, 2026-07-26).
qc = json.loads((HERE / "data_6040_2015_2026_qc.json").read_text())
def _qdate(o):
    return datetime.date(1970, 1, 1) + datetime.timedelta(days=o)
_by_year = {}
for _o, _v in qc["equity_daily"]:
    _by_year[_qdate(_o).year] = _v          # last point in each year wins
_prev = 100_000.0
for _y in sorted(_by_year):
    _v = _by_year[_y]
    rec(f"real6040_{_y}_start", _prev, f"${_prev:,.0f}", f"60/40: balance entering {_y}")
    rec(f"real6040_{_y}_pnl", _v - _prev, f"${_v - _prev:+,.0f}", f"60/40: dollars earned in {_y}")
    rec(f"real6040_{_y}_pct", (_v / _prev - 1) * 100, f"{(_v / _prev - 1) * 100:+.1f}%", f"60/40: return in {_y}")
    _prev = _v
_end = qc["equity_daily"][-1][1]
rec("real6040_end", _end, f"${_end:,.0f}", "60/40 end value Jun 2026 ($100,000 invested Jan 2015)")
rec("real6040_multiple", _end / 100_000, f"{_end / 100_000:.2f}x", "full-window multiple, Jan 2015 - Jun 2026")
rec("real6040_rate", 9.04, "9.04%", "measured compound annual return (backtest statistics)")
rec("real6040_worst_dip", -21.4, "-21.4%", "deepest fall below an earlier peak along the way (backtest statistics)")

# --- Manuscript figures (workflow step 3) ---
import math

# Lump sums, 40 years
rec("lump100k_40y_77", 100_000 * (1 + R64) ** 40, f"${rk(100_000 * (1 + R64) ** 40):,.0f}",
    "$100,000, 40y at 7.7%, no fee")
net = R64 - 0.01
rec("lump100k_40y_67net", 100_000 * (1 + net) ** 40, f"${rk(100_000 * (1 + net) ** 40):,.0f}",
    "$100,000, 40y at 6.7% (7.7% less a 1% annual fee)")
fee_lost = 1 - (1 + net) ** 40 / (1 + R64) ** 40
rec("fee1pct_40y_lost", fee_lost * 100, f"{fee_lost * 100:.0f}%",
    "share of the no-fee ending consumed by a 1% annual fee over 40y")

# Rule of 72 vs exact doubling time
for r, label in ((R2, "2"), (R64, "77"), (RSP, "99")):
    exact = math.log(2) / math.log(1 + r)
    rec(f"double_exact_{label}", exact, f"{exact:.1f}y", f"exact doubling time at {r*100:.1f}%")
    rec(f"double_rule72_{label}", 72 / (r * 100), f"{72 / (r * 100):.1f}y", f"rule of 72 at {r*100:.1f}%")

# Cost of one year of delay ($300/mo saver, read at 65)
pot26, _ = pot_and_safe(0, 300, 26, 65, R64)
rec("delay_1y_cost", potA - pot26, f"${rk(potA - pot26):,.0f}",
    "ending gap at 65: start at 25 vs start at 26 ($3,600 deposited that year)")

# Catch-up: monthly amount from 35 that matches the 25-starter at 65
annuity30 = potB / 300  # ending dollars per monthly dollar over 30y
catchup = potA / annuity30
rec("catchup_monthly_from_35", catchup, f"${catchup:,.0f}/mo",
    "monthly saving from 35 that matches $300/mo from 25, at 65")

# Three application scenarios (old deck slides 4-6): end value and the level
# monthly payout to 95 leaving a fifth of the pot (RESERVE 0.2)
for who, args in (("maya", (0, 300, 22, 65)),        # 22, $0, $300/mo, payouts 65
                  ("daniel", (50_000, 1_000, 40, 60)),  # 40, $50k, $1,000/mo, payouts 60
                  ("rosa", (1_000_000, 0, 65, 66))):    # 65, $1M, payouts now
    for r, rl in ((R2, "2"), (R64, "77"), (RSP, "99")):
        pot, safe = pot_and_safe(*args, r)
        rec(f"{who}_pot_{rl}", pot, f"${rk(pot):,.0f}", f"{who}: end value at {r*100:.1f}%")
        rec(f"{who}_safe_{rl}", safe, f"${rk(safe):,.0f}/mo", f"{who}: monthly payout to 95 at {r*100:.1f}%")

# The menu of real rates (qsl-research/demo-strategies/overview-table.md for
# the three strategies + SPY; 60/40 = the old-deck backtest average).
# Doubling times by rule of 72.
MENU = ((6.2, "defender", "The Defender, 2015-2026 window"),
        (7.7, "6040", "60/40 portfolio, 2005-2026"),
        (7.9, "spy_full", "SPY buy-and-hold, full history 1998-2026"),
        (14.1, "diversifier", "The Diversifier, 2015-2026 window"),
        (41.8, "growth_engine", "The Growth Engine, 2015-2026 window"))
for rate_pct, label, note in MENU:
    rec(f"menu_{label}", rate_pct, f"{rate_pct:.1f}%", f"average annual return: {note}")
    rec(f"double_{label}", 72 / rate_pct, f"{72 / rate_pct:.1f}y",
        f"rule-of-72 doubling time: {note}")

# Catch-up rates: the annual return that makes $300/mo from a later start
# reach the 25-starter's raw ending (potA) at 65. Bisection on the rate.
def fv_monthly(monthly, years, rate):
    rm = (1 + rate) ** (1 / 12) - 1
    g = (1 + rm) ** (years * 12)
    return monthly * ((g - 1) / rm)

def required_rate(target, monthly, years):
    lo, hi = 0.001, 1.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if fv_monthly(monthly, years, mid) < target: lo = mid
        else: hi = mid
    return (lo + hi) / 2

for start_age in (35, 40, 45):
    yrs = 65 - start_age
    r = required_rate(potA, 300, yrs)
    rec(f"catchup_rate_from_{start_age}", r * 100, f"{r*100:.1f}%",
        f"rate for $300/mo from {start_age} to match the 25-starter at 65 ({yrs}y)")

with (HERE / "data_unit1_compounding.csv").open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "value", "display", "note"])
    w.writeheader()
    w.writerows(rows)

# --- Slide-1 chart: yearly balances, both savers, viewBox 1000x420 ---
balA = balances(300, 40, R64)                 # ages 26..65
balB = [0.0] * 10 + balances(300, 30, R64)    # flat zero to 35, then 30y
top = max(balA) * 1.04
def pts(series):
    n = len(series) - 1
    return " ".join(f"{i / n * 1000:.1f},{420 - v / top * 420:.1f}"
                    for i, v in enumerate(series))
with (HERE / "chart_points.txt").open("w") as f:
    f.write("EARLY (start 25):\n" + pts([0.0] + balA) + "\n\n")
    f.write("LATE (start 35):\n" + pts([0.0] + balB) + "\n\n")
    f.write(f"y-axis top = {top:,.0f}\n")
    for gl in (250_000, 500_000, 750_000):
        f.write(f"gridline {gl:,}: y = {420 - gl / top * 420:.1f}\n")

print(f"{len(rows)} rows -> data_unit1_compounding.csv")
for r in rows:
    print(f"  {r['name']:24s} {r['display']:>12s}  {r['note']}")
