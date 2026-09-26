from backend.db import connect

def test_retried_payment_is_not_duplicated(client, seed_invoice, db_path):
    invoice_id = seed_invoice()
    payload = {'invoice_id':invoice_id,'amount_paise':5000,'request_key':'retry-123'}
    first = client.post('/payments', json=payload)
    second = client.post('/payments', json=payload)
    assert first.status_code == second.status_code == 201
    assert first.json()['id'] == second.json()['id']
    with connect(db_path) as db:
        assert db.execute('SELECT COUNT(*) FROM payments').fetchone()[0] == 1
    changed = dict(payload, amount_paise=6000)
    assert client.post('/payments', json=changed).status_code == 409
