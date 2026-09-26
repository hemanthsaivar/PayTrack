def test_missing_invoice_is_404(client, seed_invoice):
    existing = seed_invoice()
    assert client.get(f'/invoices/{existing}').status_code == 200
    assert client.get('/invoices/99999').status_code == 404
