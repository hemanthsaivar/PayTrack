import pytest
from fastapi.testclient import TestClient
from backend.main import create_app
from backend.db import connect

@pytest.fixture
def db_path(tmp_path):
    return tmp_path / 'test.db'

@pytest.fixture
def client(db_path):
    with TestClient(create_app(db_path)) as client:
        yield client

@pytest.fixture
def seed_invoice(client, db_path):
    def seed(customer='Demo', amount=10000, status='open', note=''):
        with connect(db_path) as db:
            cur = db.execute('INSERT INTO invoices(customer,amount_paise,status,note) VALUES (?,?,?,?)',
                             (customer,amount,status,note))
            db.commit()
            return cur.lastrowid
    return seed

@pytest.fixture
def seed_payment(seed_invoice, db_path):
    def seed(amount=10000, status='success', refunded=0):
        invoice_id = seed_invoice()
        with connect(db_path) as db:
            cur = db.execute('INSERT INTO payments(invoice_id,amount_paise,status,request_key,refunded_paise) VALUES (?,?,?,?,?)',
                             (invoice_id,amount,status,'fixture',refunded))
            db.commit()
            return cur.lastrowid
    return seed
