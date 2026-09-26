def test_note_survives_new_connection(client, seed_invoice):
    invoice_id = seed_invoice()
    assert client.patch(f'/invoices/{invoice_id}/note', json={'note':'Call tomorrow'}).status_code == 200
    assert client.get(f'/invoices/{invoice_id}').json()['note'] == 'Call tomorrow'
