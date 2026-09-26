# Day 7 — Refunds exceed original payment

**Timebox:** 60 minutes. Work on this ticket only.

## Bug report
A ₹100 payment accepts refunds of ₹70 and ₹40.

## Reproduce
Use the test fixture, refund 7000 paise, then 4000 paise.

Run from the project root:
```bash
python -m pytest tests/test_day07.py -q
```

## Acceptance criteria
Second refund returns 409 without modifying data. Refunding the remaining 3000 succeeds. Failed payments remain nonrefundable.

## Suggested investigation area
`backend/repository.py`. Trace the relevant route; you do not need to read the whole app.

## Parallel learning (inside the hour)
Business invariants; boundary conditions. Explain the concept in two sentences in your progress log.

<details>
<summary>Optional hint — open after 15 minutes stuck</summary>

Compare the new request to the remaining refundable balance.
</details>

## Hand-in
Send your changed code, test output, and one sentence on the root cause. Stop at 60 minutes.
