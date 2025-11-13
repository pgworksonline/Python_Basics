txns = [1.09, 23.56, 56.89, 77.23, 7.77]
TAX_RATE = 0.08

def get_price_with_tax(txn):
    return txn * (1 * TAX_RATE)

final_prices = map(get_price_with_tax, txns)
list(final_prices)
