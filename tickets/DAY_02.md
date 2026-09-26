# Day 2 — Zero quantity accepted

**Timebox:** 60 minutes. Work on this ticket only.

## Bug report
The API accepts an invoice line with quantity 0.

## Reproduce
POST /invoices with quantity 0, then -1, 1.5, and the string "2".

Run from the project root:
```bash
python -m pytest tests/test_day02.py -q
```

## Acceptance criteria
All four invalid values return 422. Positive integer quantities still return 201.

## Suggested investigation area
`backend/schemas.py`. Trace the relevant route; you do not need to read the whole app.

## Parallel learning (inside the hour)
Pydantic validation; HTTP 422. Explain the concept in two sentences in your progress log.

<details>
<summary>Optional hint — open after 15 minutes stuck</summary>

Compare inclusive and exclusive field boundaries.
</details>

## Hand-in
Send your changed code, test output, and one sentence on the root cause. Stop at 60 minutes.
