# Criar coluna de hora a partir do InvoiceDate
X['InvoiceDate'] = pd.to_datetime(X['InvoiceDate'])
def periodo(hora):
  if hora >= 6 and hora < 12:
    return 'Morning'
  elif hora >= 12 and hora < 18:
    return 'Afternoon'
  else:
    return 'Evening'
X['Period'] = X['InvoiceDate'].dt.hour.apply(periodo)