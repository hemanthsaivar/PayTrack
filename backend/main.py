import os
from pathlib import Path
from typing import Literal
from fastapi import FastAPI, Query
from fastapi.responses import Response
from backend.db import initialize
from backend import repository as repo
from backend.schemas import InvoiceCreate, NoteUpdate, PaymentCreate, RefundCreate
from backend.exporting import invoice_csv

def create_app(db_path=None):
    path = str(db_path or os.environ.get('PAYTRACK_DB', 'data/paytrack.db'))
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    initialize(path)
    app = FastAPI(title='PayTrack Debugging Lab', version='0.1.0')

    @app.get('/health')
    def health():
        return {'status': 'ok'}

    @app.post('/invoices', status_code=201)
    def create_invoice(payload: InvoiceCreate):
        return repo.create_invoice(path, payload)

    @app.get('/invoices')
    def list_invoices(status: Literal['open','paid'] | None = None,
                      limit: int = Query(20, ge=1, le=100), offset: int = Query(0, ge=0)):
        return repo.list_invoices(path, status, limit, offset)

    @app.get('/invoices/{invoice_id}')
    def get_invoice(invoice_id: int):
        return repo.get_invoice(path, invoice_id)

    @app.patch('/invoices/{invoice_id}/note')
    def update_note(invoice_id: int, payload: NoteUpdate):
        return repo.update_note(path, invoice_id, payload.note)

    @app.post('/payments', status_code=201)
    def create_payment(payload: PaymentCreate):
        return repo.create_payment(path, payload)

    @app.post('/payments/{payment_id}/refund')
    def refund(payment_id: int, payload: RefundCreate):
        return repo.refund_payment(path, payment_id, payload.amount_paise)

    @app.get('/reports/summary')
    def summary():
        return repo.summary(path)

    @app.get('/reports/invoices.csv')
    def export():
        return Response(invoice_csv(repo.all_invoices(path)), media_type='text/csv')

    return app
