def test_total_respects_quantity(client):
    response = client.post('/invoices', json={'customer':'Asha','items':[
        {'description':'Book','unit_price_paise':25000,'quantity':3},
        {'description':'Pen','unit_price_paise':10000,'quantity':2}]})
    assert response.status_code == 201
    assert response.json()['amount_paise'] == 95000
