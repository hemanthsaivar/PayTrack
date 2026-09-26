# Day 3 — Missing invoice looks successful

**Timebox:** 60 minutes. Work on this ticket only.

## Bug report
Looking up invoice 99999 returns HTTP 200 and an empty object.

## Reproduce
GET /invoices/99999 on a fresh database.

Run from the project root:
```bash
python -m pytest tests/test_day03.py -q
```

## Acceptance criteria
Missing IDs return 404 with a useful detail; existing IDs return 200.

## Suggested investigation area
`backend/repository.py`. Trace the relevant route; you do not need to read the whole app.

## Parallel learning (inside the hour)
Exceptions; HTTP semantics. Explain the concept in two sentences in your progress log.

<details>
<summary>Optional hint — open after 15 minutes stuck</summary>

What should the repository do when fetchone returns None?
</details>

## Hand-in
Send your changed code, test output, and one sentence on the root cause. Stop at 60 minutes.
