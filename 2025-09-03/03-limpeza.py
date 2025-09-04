#LIMPEZA
#RELEMBRANDO: loja online do Reino Unido, vendas realizadas entre 01/09/2010 e 09/12/2011

#REMOVER LINHAS SEM CLIENTES
data_cleaned = data.dropna(subset=['CustomerID'])
#remover valores nulos na tabela do cliente


#REMOVER DEVOLUÇÕES
data_cleaned = data_cleaned[data_cleaned['Quantity'] > 0]
data_cleaned = data_cleaned[data_cleaned['UnitPrice'] > 0]
#remover números menores de zero


#CRIAR VARIÁVEL VALOR TOTAL
data_cleaned['TotalValue'] = data_cleaned['Quantity'] * data_cleaned['UnitPrice']
#quantiddae*valor unitário


#CONVERTER DATA PARA DATETIME
data_cleaned['Year'] = pd.to_datetime(data_cleaned['InvoiceDate'])