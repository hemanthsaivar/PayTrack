# PayTrack — 10-day debugging project

A runnable Python + FastAPI + Streamlit + SQLite application with **10 intentional bugs**.
Your job is to repair an existing codebase, one ticket per day, rather than build everything from scratch.
This is a substantial learning project scoped to ten one-hour sessions, not a production payment system.
All transactions are simulated. No accounts, API keys, real cards, Docker, or cloud services are needed.

## Start here (Mac / Linux)

Use Python 3.11 or 3.12. Extract the ZIP and open a terminal inside `PayTrack`.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python seed.py
python -m pytest tests/test_smoke.py -q
python -m uvicorn backend.main:create_app --factory --reload --host 127.0.0.1 --port 8000
```

In a second terminal, enter the same folder and run:

```bash
source .venv/bin/activate
python -m streamlit run frontend/app.py --server.address 127.0.0.1
```

Open the dashboard at http://localhost:8501 and API playground at http://127.0.0.1:8000/docs.
On Windows use `py -3.11 -m venv .venv` and `.venv\Scripts\activate` instead.
The dependency versions are a fixed lab baseline, not a claim that they are the newest versions.
If installation fails, send the error; do not spend the whole session troubleshooting tooling.

## Daily limit: 60 minutes

Days 2–9: 10 minutes reading/learning, 10 reproducing, 25 fixing, 10 testing, 5 logging.
Day 1: 20 minutes setup, 10 exploring/reproducing, 20 fixing, 5 testing, 5 logging.
Day 10: 10 minutes reading/reproducing, 25 fixing, 20 regression, 5 logging.
**Stop at 60 minutes even if the bug remains.** Record the blocker and ask for one hint.
Do not borrow time from your other studies. If setup uses Day 1, stop and move the ticket to the next session.
These are effort estimates, not guaranteed completion times.

Read only today's file in `tickets/`. Run only today's test initially:

```bash
python -m pytest tests/test_day01.py -q
```

Replace `01` with the day number. Red tests at the start are expected. Do not change tests to make them green.
Tests use isolated temporary databases, never your dashboard database. Most tickets can be solved independently.
After fixing, add one small edge-case test if time permits. Use remaining test time to rerun earlier days.
On Day 10 run `python -m pytest -q`. Optional Git checkpoints: `git init`, then commit each day's changes.

## Code map

| Location | Responsibility |
|---|---|
| backend/main.py | App factory and API routes |
| backend/schemas.py | Request validation |
| backend/calculations.py | Invoice arithmetic |
| backend/repository.py | SQLite reads, writes, payment rules, reports |
| backend/db.py | Schema and connection lifecycle |
| backend/exporting.py | CSV serialization |
| frontend/app.py | Four Streamlit screens |
| frontend/client.py | HTTP API client and timeouts |
| frontend/state.py | Session defaults |
| seed.py | Six demo invoices and three payments |
| tests/ | Smoke checks and one ticket suite per day |

Request flow: Streamlit calls FastAPI; FastAPI validates input and calls the repository; the repository uses SQLite.
Amounts are integer paise to avoid floating-point money calculations. ₹250 is 25000 paise.
Invoice statuses are preset for filtering exercises; payments do not auto-settle invoices in this lab.
Partial or excess payments may be recorded because settlement rules are outside this challenge.
No authentication or concurrent payment guarantees are implemented. Keep this deliberately buggy lab local.

## Expected starter state

Two smoke tests pass. Each of the ten day files has an intended failure; three Day 2 invalid-input cases already pass.
No syntax or startup failure is intentional. If the app cannot start, ask for help instead of treating it as a ticket.
The seed report should show ₹1000 after Day 8 is fixed. Seeding again preserves existing data.
To reset demo data: stop both apps, delete only `data/paytrack.db`, run `python seed.py`, then restart.

## After each session

Fill in `PROGRESS.md`. Send me today's changed function(s), test output and your explanation.
Ask: “Review my Day 1 fix. Give hints only if it is wrong.” You do not need to upload the whole project.

## Ten-day roadmap

| Day | Bug | Learning focus |
|---|---|---|
| 1 | Incorrect invoice total | Tracing function calls; generator expressions |
| 2 | Zero quantity accepted | Pydantic validation; HTTP 422 |
| 3 | Missing invoice looks successful | Exceptions; HTTP semantics |
| 4 | Notes disappear | SQLite transactions; connection lifecycle |
| 5 | Filtered pages are incomplete | SQL WHERE, ORDER BY, LIMIT and OFFSET |
| 6 | Payment retries create duplicates | Idempotency; payload comparison |
| 7 | Refunds exceed original payment | Business invariants; boundary conditions |
| 8 | Dashboard includes failed payments | SQL aggregation; test fixtures |
| 9 | Streamlit filter resets | Streamlit reruns; session state; mocking |
| 10 | CSV columns and rows break | CSV serialization; regression testing |

## Reference reading — optional, inside the daily learning slot

- Python tutorial: https://docs.python.org/3/tutorial/
- SQLite transactions: https://docs.python.org/3/library/sqlite3.html
- FastAPI testing: https://fastapi.tiangolo.com/tutorial/testing/
- Pydantic fields: https://docs.pydantic.dev/latest/concepts/fields/
- Streamlit testing: https://docs.streamlit.io/develop/concepts/app-testing
- Streamlit session state: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
- CSV module: https://docs.python.org/3/library/csv.html

Finished solutions are intentionally omitted. The bug reports and tests are your specification.
After ten days, possible separate projects include authentication, concurrent idempotency with unique constraints,
automatic invoice settlement, Docker, and deployment. They are not part of this ten-hour commitment.
