#RFM
#Recency (há quanto tempo comprou)
#Frequency (quantas vezes comprou)
#Monetary (quanto pagou)

quantiles = features[['Recency', 'Frequency', 'Monetary_Total']].quantile(q=[0.25, 0.5, 0.75]).to_dict()
quantiles