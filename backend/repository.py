from fastapi import HTTPException
from backend.db import connect
from backend.calculations import invoice_total

def create_invoice(path, payload):
    with connect(path) as db:
        cur = db.execute('INSERT INTO invoices(customer, amount_paise) VALUES (?, ?)',
                         (payload.customer, invoice_total(payload.items)))
        db.commit()
        return dict(db.execute('SELECT * FROM invoices WHERE id=?', (cur.lastrowid,)).fetchone())

def get_invoice(path, invoice_id):
    with connect(path) as db:
        row = db.execute('SELECT * FROM invoices WHERE id=?', (invoice_id,)).fetchone()
        if row is None:
            raise HTTPException(404, 'Invoice not found')
        return dict(row)

def update_note(path, invoice_id, note):
    with connect(path) as db:
        cur = db.execute('UPDATE invoices SET note=? WHERE id=?', (note, invoice_id))
        if cur.rowcount == 0:
            raise HTTPException(404, 'Invoice not found')
        row = db.execute('SELECT * FROM invoices WHERE id=?', (invoice_id,)).fetchone()
        db.commit()
        return dict(row)

def list_invoices(path, status=None, limit=20, offset=0):
    with connect(path) as db:
        rows = db.execute('SELECT * FROM invoices ORDER BY id LIMIT ? OFFSET ?',
                          (limit, offset)).fetchall()
        result = [dict(row) for row in rows]
        if status:
            result = [row for row in result if row['status'] == status]
        return result

def create_payment(path, payload):
    with connect(path) as db:
        if not db.execute('SELECT id FROM invoices WHERE id=?', (payload.invoice_id,)).fetchone():
            raise HTTPException(404, 'Invoice not found')
        status = 'failed' if payload.simulate_failure else 'success'
        cur = db.execute('INSERT INTO payments(invoice_id,amount_paise,status,request_key) VALUES (?,?,?,?)',
                         (payload.invoice_id, payload.amount_paise, status, payload.request_key))
        db.commit()
        return dict(db.execute('SELECT * FROM payments WHERE id=?', (cur.lastrowid,)).fetchone())

def refund_payment(path, payment_id, amount):
    with connect(path) as db:
        row = db.execute('SELECT * FROM payments WHERE id=?', (payment_id,)).fetchone()
        if row is None:
            raise HTTPException(404, 'Payment not found')
        if row['status'] != 'success':
            raise HTTPException(409, 'Only successful payments can be refunded')
        if amount > row['amount_paise']:
            raise HTTPException(409, 'Refund exceeds remaining amount')
        db.execute('UPDATE payments SET refunded_paise=refunded_paise+? WHERE id=?', (amount,payment_id))
        db.commit()
        return dict(db.execute('SELECT * FROM payments WHERE id=?', (payment_id,)).fetchone())

def summary(path):
    with connect(path) as db:
        row = db.execute('SELECT COALESCE(SUM(amount_paise-refunded_paise),0) AS net_paise FROM payments').fetchone()
        return dict(row)

def all_invoices(path):
    with connect(path) as db:
        return [dict(row) for row in db.execute('SELECT * FROM invoices ORDER BY id')]
