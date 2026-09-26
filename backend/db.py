import sqlite3
from contextlib import contextmanager

SCHEMA = """
CREATE TABLE IF NOT EXISTS invoices (
 id INTEGER PRIMARY KEY, customer TEXT NOT NULL, amount_paise INTEGER NOT NULL,
 status TEXT NOT NULL DEFAULT 'open', note TEXT NOT NULL DEFAULT ''
);
CREATE TABLE IF NOT EXISTS payments (
 id INTEGER PRIMARY KEY, invoice_id INTEGER NOT NULL REFERENCES invoices(id),
 amount_paise INTEGER NOT NULL, status TEXT NOT NULL, request_key TEXT NOT NULL,
 refunded_paise INTEGER NOT NULL DEFAULT 0
);
"""

@contextmanager
def connect(path):
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA foreign_keys=ON')
    try:
        yield db
    finally:
        db.close()

def initialize(path):
    with connect(path) as db:
        db.executescript(SCHEMA)
        db.commit()
