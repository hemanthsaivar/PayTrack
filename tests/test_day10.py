import csv
import io

def test_csv_round_trip(client, seed_invoice):
    name = 'Acme, "India"'
    note = 'First line\nSecond line'
    seed_invoice(customer=name, note=note)
    response = client.get('/reports/invoices.csv')
    assert response.status_code == 200
    rows = list(csv.DictReader(io.StringIO(response.text)))
    assert len(rows) == 1
    assert rows[0]['customer'] == name
    assert rows[0]['note'] == note
    assert set(rows[0]) == {'id','customer','amount_paise','status','note'}
