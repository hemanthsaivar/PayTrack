# Day 5 — Filtered pages are incomplete

**Timebox:** 60 minutes. Work on this ticket only.

## Bug report
Paid invoices exist, but a two-row page contains only one row.

## Reproduce
Use the six alternating open/paid invoices created by the test; request paid limit=2 offsets 0 and 2.

Run from the project root:
```bash
python -m pytest tests/test_day05.py -q
```

## Acceptance criteria
The first page contains IDs 2 and 4, the next contains 6. Ordering is stable. Filtering precedes pagination.

## Suggested investigation area
`backend/repository.py`. Trace the relevant route; you do not need to read the whole app.

## Parallel learning (inside the hour)
SQL WHERE, ORDER BY, LIMIT and OFFSET. Explain the concept in two sentences in your progress log.

<details>
<summary>Optional hint — open after 15 minutes stuck</summary>

Which happens first: selecting a page, or narrowing the matching records?
</details>

## Hand-in
Send your changed code, test output, and one sentence on the root cause. Stop at 60 minutes.
