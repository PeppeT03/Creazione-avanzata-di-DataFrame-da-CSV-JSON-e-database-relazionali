import pandas as pd

# Creiamo un file CSV fittizio per l'esercizio
dati = {
    "date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05"],
    "product_id": ["P1", "P2", "P1", "P3", "P2"],
    "qty": [10, 5, 8, 3, 12],
    "price": [15.5, 20.0, 15.5, 50.0, 20.0]
}
df_setup = pd.DataFrame(dati)
df_setup.to_csv("transactions.csv", index=False)
print("File 'transactions.csv' creato con successo!")