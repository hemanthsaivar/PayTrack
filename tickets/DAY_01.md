# Day 1 — Incorrect invoice total

**Timebox:** 60 minutes. Work on this ticket only.

## Bug report
A customer buys three items at ₹250 each and two at ₹100. The invoice shows ₹350 instead of ₹950.

## Reproduce
POST /invoices with the two lines from tests/test_day01.py. Inspect amount_paise.

Run from the project root:
```bash
python -m pytest tests/test_day01.py -q
```

## Acceptance criteria
The response total is 95000 paise. Multiple lines and quantity 1 still work.

## Suggested investigation area
`backend/calculations.py`. Trace the relevant route; you do not need to read the whole app.

## Parallel learning (inside the hour)
Tracing function calls; generator expressions. Explain the concept in two sentences in your progress log.

<details>
<summary>Optional hint — open after 15 minutes stuck</summary>

Trace request → schema → repository → calculation. Which input is unused?
</details>

## Hand-in
Send your changed code, test output, and one sentence on the root cause. Stop at 60 minutes.
