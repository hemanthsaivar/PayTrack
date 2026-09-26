def test_cumulative_refunds(client, seed_payment):
    payment_id = seed_payment(amount=10000)
    url = f'/payments/{payment_id}/refund'
    assert client.post(url, json={'amount_paise':7000}).status_code == 200
    assert client.post(url, json={'amount_paise':4000}).status_code == 409
    last = client.post(url, json={'amount_paise':3000})
    assert last.status_code == 200
    assert last.json()['refunded_paise'] == 10000
