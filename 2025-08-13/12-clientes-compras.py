# Cliente com maior número de compras
cliente_mais_compras = df.groupby('CustomerID')['InvoiceNo'].nunique().sort_values(ascending=False).head(1)
cliente_id = cliente_mais_compras.index[0]
print("Cliente com mais compras:")
print(cliente_mais_compras)