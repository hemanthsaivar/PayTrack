# Day 9 — Streamlit filter resets

**Timebox:** 60 minutes. Work on this ticket only.

## Bug report
Checking Show paid invoices only does not stay selected across reruns.

## Reproduce
Open Invoices, check the paid-only checkbox, then click Refresh. The automated test mocks the API.

Run from the project root:
```bash
python -m pytest tests/test_day09.py -q
```

## Acceptance criteria
Checkbox selection survives reruns. A fresh session defaults to False. Do not replace the session state with a module global.

## Suggested investigation area
`frontend/state.py and frontend/app.py`. Trace the relevant route; you do not need to read the whole app.

## Parallel learning (inside the hour)
Streamlit reruns; session state; mocking. Explain the concept in two sentences in your progress log.

<details>
<summary>Optional hint — open after 15 minutes stuck</summary>

Initialization should set a default only when the key is absent.
</details>

## Hand-in
Send your changed code, test output, and one sentence on the root cause. Stop at 60 minutes.
