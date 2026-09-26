# Day 6 — Payment retries create duplicates

**Timebox:** 60 minutes. Work on this ticket only.

## Bug report
Retrying the same payment request records another payment.

## Reproduce
POST the same invoice_id, amount_paise and request_key twice.

Run from the project root:
```bash
python -m pytest tests/test_day06.py -q
```

## Acceptance criteria
Same key plus identical payload returns the original row and ID (201 for both in this lab). Same key with changed invoice, amount or simulate_failure returns 409. A new key creates a new row.

## Suggested investigation area
`backend/repository.py`. Trace the relevant route; you do not need to read the whole app.

## Parallel learning (inside the hour)
Idempotency; payload comparison. Explain the concept in two sentences in your progress log.

<details>
<summary>Optional hint — open after 15 minutes stuck</summary>

Look up an existing request_key before inserting. Compare the full business payload. Sequential retries only are in scope today.
</details>

## Hand-in
Send your changed code, test output, and one sentence on the root cause. Stop at 60 minutes.
