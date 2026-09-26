import pytest
@pytest.mark.parametrize('quantity', [0, -1, 1.5, '2'])
def test_invalid_quantity(client, quantity):
    response = client.post('/invoices', json={'customer':'Demo','items':[
        {'description':'Book','unit_price_paise':100,'quantity':quantity}]})
    assert response.status_code == 422
