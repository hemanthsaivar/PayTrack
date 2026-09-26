from pathlib import Path
from backend.db import initialize, connect

path = 'data/paytrack.db'
Path('data').mkdir(exist_ok=True)
initialize(path)
with connect(path) as db:
    if db.execute('SELECT COUNT(*) FROM invoices').fetchone()[0]:
        print('Existing data retained; seed skipped.')
    else:
        db.executemany('INSERT INTO invoices(customer,amount_paise,status,note) VALUES (?,?,?,?)', [
            ('Asha', 25000, 'open', ''), ('Hemanth', 30000, 'paid', 'Demo settled invoice'),
            ('Ravi', 10000, 'open', ''), ('Acme, India', 75000, 'paid', 'First line\nSecond line'),
            ('Meera', 20000, 'open', ''), ('Dev', 40000, 'paid', '')])
        db.executemany('INSERT INTO payments(invoice_id,amount_paise,status,request_key,refunded_paise) VALUES (?,?,?,?,?)', [
            (2,30000,'success','seed-1',0), (4,75000,'success','seed-2',5000),
            (3,10000,'failed','seed-3',0)])
        db.commit()
        print('Seeded 6 invoices and 3 payments. Expected net collected: 100000 paise (₹1000).')
