# Day 8 — Dashboard includes failed payments

**Timebox:** 60 minutes. Work on this ticket only.

## Bug report
The report counts failed payment attempts as money received.

## Reproduce
Seed successful payments of 10000 (2000 refunded) and 5000, plus a failed 7000.

Run from the project root:
```bash
python -m pytest tests/test_day08.py -q
```

## Acceptance criteria
Net collected is 13000 paise. Empty database reports 0. Refunds are deducted from successful payments only.

## Suggested investigation area
`backend/repository.py`. Trace the relevant route; you do not need to read the whole app.

## Parallel learning (inside the hour)
SQL aggregation; test fixtures. Explain the concept in two sentences in your progress log.

<details>
<summary>Optional hint — open after 15 minutes stuck</summary>

Which payment statuses belong in revenue?
</details>

## Hand-in
Send your changed code, test output, and one sentence on the root cause. Stop at 60 minutes.
