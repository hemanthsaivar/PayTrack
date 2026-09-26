def test_health(client):
    assert client.get('/health').json() == {'status':'ok'}

def test_simple_invoice(client):
    response = client.post('/invoices', json={'customer':'Demo','items':[
        {'description':'Book','unit_price_paise':100,'quantity':1}]})
    assert response.status_code == 201
    assert response.json()['amount_paise'] == 100
