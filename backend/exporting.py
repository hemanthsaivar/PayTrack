def invoice_csv(rows):
    lines = ['id,customer,amount_paise,status,note']
    for row in rows:
        lines.append(','.join(str(row[key]) for key in ['id','customer','amount_paise','status','note']))
    return '\n'.join(lines) + '\n'
