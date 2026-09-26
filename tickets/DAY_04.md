# Day 4 — Notes disappear

**Timebox:** 60 minutes. Work on this ticket only.

## Bug report
Saving a note appears successful, but refreshing loses the change.

## Reproduce
Create an invoice, PATCH its note, then GET the invoice in a new request.

Run from the project root:
```bash
python -m pytest tests/test_day04.py -q
```

## Acceptance criteria
The saved note survives a new connection and API restart. Missing IDs remain 404.

## Suggested investigation area
`backend/repository.py and backend/db.py`. Trace the relevant route; you do not need to read the whole app.

## Parallel learning (inside the hour)
SQLite transactions; connection lifecycle. Explain the concept in two sentences in your progress log.

<details>
<summary>Optional hint — open after 15 minutes stuck</summary>

A successful UPDATE is not necessarily a persisted UPDATE.
</details>

## Hand-in
Send your changed code, test output, and one sentence on the root cause. Stop at 60 minutes.
