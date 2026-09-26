def test_summary_excludes_failed_payments(client, seed_payment):
    assert client.get('/reports/summary').json()['net_paise'] == 0
    seed_payment(amount=10000, refunded=2000)
    seed_payment(amount=7000, status='failed')
    seed_payment(amount=5000)
    assert client.get('/reports/summary').json()['net_paise'] == 13000
