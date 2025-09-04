#ANÁLISE, INFERÊNCIA
#Criar colunas, informações

snapshot_date = data_cleaned['Year'].max() + pd.Timedelta(days=1)
#data base, um dia após a última compra (ou seja, dia 10/12/2011)


#ARUPAMENTO POR CLIENTE
#há quanto tempo a compra foi realizada (em relação a data base)
features = data_cleaned.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days, #recency
    'InvoiceNo': 'count',                                    #frequency
    'TotalValue': ['sum', 'mean'],                           #monetary total and average
    'StockCode': 'nunique',                                  #variety
    'Country': 'first'                                       #country
})
features.columns = ['Recency', 'Frequency', 'Monetary_Total', 'Monetary_Average', 'Variety', 'Country']

features['Country'] = LabelEncoder().fit_transform(features['Country'])

features