import pandas as pd

dati = pd.read_csv("transactions.csv",parse_dates=['date'],dtype={'product_id':'category'})

dati['revenue'] = dati['qty'] * dati['price']

top_5 = dati.sort_values(by="revenue",ascending=False)

print(top_5)