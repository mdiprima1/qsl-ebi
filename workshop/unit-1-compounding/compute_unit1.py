#!/usr/bin/env python3
"""Unit 1 (Compounding) — data generator for the workshop draft.

Reproduces the calculator from the old free-course Unit 1 deck
(qsl-hq/blueprint/COURSE-FREE/unit-1/build_unit1.py) so every number
shown on the slides traces to this file's output.

Outputs:
  data_unit1_compounding.csv   every figure used on the slides
  chart_points.txt             SVG polyline coordinates for the slide-1 chart

Rates (inputs, carried from the old deck, provenance as recorded there):
  2.0%  savings account
  7.7%  60/40 portfolio average annual return, 2005-2026 (QSL backtest)
  9.9%  S&P 500 average annual return, 2005-2026 (QSL backtest)
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
R2, R64, RSP = 0.02, 0.077, 0.099
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
for r, label, note in ((R2, "rate2", "2.0% savings account"),
                       (R64, "rate77", "7.7% 60/40 portfolio 2005-2026"),
                       (RSP, "rate99", "9.9% S&P 500 2005-2026")):
    pot = pot_and_safe(0, 500, 25, 65, r)[0]
    rec(f"t500_{label}", pot, f"${rk(pot):,.0f}", f"$500/mo, 40y at {note}")

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
