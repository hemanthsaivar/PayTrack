def invoice_total(items):
    return sum(item.unit_price_paise * item.quantity for item in items)
