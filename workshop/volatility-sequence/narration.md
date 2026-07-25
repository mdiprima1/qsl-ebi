# Narration — volatility, the five-slide sequence

One block per slide. Each block ends with a spoken summary (the shortest restatement of the slide in slightly different words). Every number matches `data_202605_aapl_tsla.csv`.

---

## Slide 1 — Two stocks, one return (Scenario)

Let's start with two stocks and what they did in May 2026.

AAPL ended the month up 11.5%.

TSLA ended the same month up 11.5% as well. To within one hundredth of a percent, the two returns were the same.

The chart shows the path each stock took to that result. Both start at 100, and both end in the same place.

Now look at the two paths and answer this before the next slide. Were the two investments equally risky? And if not — how would you put a number on the difference? Pause here and decide on an answer.

**Summary:** Two stocks, the same month, the same return. The question is whether they carried the same risk, and how that could be measured.

---

## Slide 2 — The typical size of a daily move (Intuition)

Let's try to answer that question.

One natural answer is to compare the worst single day. TSLA's worst day in May 2026 was a loss of 4.75%. AAPL's was a loss of 1.18%.

That answer points the right way, but a single day is one event, not a pattern. A stock could have one bad day in an otherwise calm month.

A better measure describes every day in the period: the typical size of a daily move.

On a typical day in May 2026, TSLA moved 2.1% up or down. AAPL moved 0.9%. The two stocks differed in risk, not in return.

**Summary:** One bad day is not a pattern. The measure we want is the typical size of a daily move, and in May 2026 TSLA's typical move was more than twice AAPL's.

---

## Slide 3 — Volatility (Definition)

This idea has a name.

Volatility is the typical size of the moves in an investment's value over a chosen period.

The formal measure is the standard deviation of the returns for that period. The formula on the right computes it.

In the formula, r with the small i is each period's return — for example, one day's percentage change. r with the bar is the average of those returns. N is how many returns the period contains. And sigma, the result, is the volatility: one number for the whole period.

Read the formula as a sentence: how far does a typical return sit from the average return?

**Summary:** Volatility is the typical size of a move, measured as the standard deviation of the period's returns.

---

## Slide 4 — Calculating volatility for AAPL and TSLA (Worked example)

Let's calculate it for our two stocks.

Take each trading day's percentage change in value. The bars show all twenty trading days of May 2026 for each stock, drawn on the same scale.

Find the average daily return. Then measure how far each day sits from that average.

The standard deviation of those daily returns is the daily volatility. For May 2026, AAPL's was 0.94%. TSLA's was 2.49%.

TSLA's volatility was more than two and a half times AAPL's. This is the number the question on the first slide asked for. With one number per investment, the risk of any two investments can be compared directly.

**Summary:** Daily returns, their average, the standard deviation. AAPL 0.94%, TSLA 2.49%. One number per stock, and the difference in risk can be measured.

---

## Slide 5 — What volatility does and does not tell you (Considerations)

Before moving on, keep four things in mind about volatility.

First, volatility counts moves in both directions. A sharp rise raises it as much as a sharp fall. It measures the size of moves, not falling prices.

Second, volatility carries the time scale of its returns. Daily returns give daily volatility. The convention for comparing investments is the annualized figure: the daily number scaled by the square root of 252 trading days, a factor of about sixteen.

Third, volatility describes the period it was measured on. May's volatility is a fact about May. Volatility changes over time, and calm months can be followed by rough ones.

Fourth, one number cannot show the shape of the moves. Steady daily swings and rare large drops can produce the same volatility. Later units measure that difference.

**Summary:** Volatility measures both directions, carries its time scale, describes only the period it was measured on, and says nothing about the shape of the moves.

One question to close. Suppose two funds both returned 8% over the same year. One had a volatility of 5%, the other of 15%. What does that difference tell you about the path each fund took?
