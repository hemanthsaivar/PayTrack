def test_filter_before_pagination(client, seed_invoice):
    for i in range(6):
        seed_invoice(status='paid' if i % 2 else 'open')
    first = client.get('/invoices', params={'status':'paid','limit':2,'offset':0}).json()
    second = client.get('/invoices', params={'status':'paid','limit':2,'offset':2}).json()
    assert [row['id'] for row in first] == [2,4]
    assert [row['id'] for row in second] == [6]
