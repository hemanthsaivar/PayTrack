# Day 10 — CSV columns and rows break

**Timebox:** 60 minutes. Work on this ticket only.

## Bug report
Customer names containing commas or quotes shift columns; multiline notes create extra rows.

## Reproduce
Export an invoice for Acme, "India" with a two-line note and parse it with csv.DictReader.

Run from the project root:
```bash
python -m pytest tests/test_day10.py -q
```

## Acceptance criteria
A CSV reader reconstructs one row with the exact original customer and note. Header order remains id,customer,amount_paise,status,note. Run the complete regression suite.

## Suggested investigation area
`backend/exporting.py`. Trace the relevant route; you do not need to read the whole app.

## Parallel learning (inside the hour)
CSV serialization; regression testing. Explain the concept in two sentences in your progress log.

<details>
<summary>Optional hint — open after 15 minutes stuck</summary>

Use the Python CSV module and an in-memory text buffer instead of concatenating fields.
</details>

## Hand-in
Send your changed code, test output, and one sentence on the root cause. Stop at 60 minutes.
