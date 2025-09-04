features['RecencyScore'] = features['Recency'].apply(rfm_score, args=(quantiles, 'Recency', True)) #valor invertido
features['FrequencyScore'] = features['Frequency'].apply(rfm_score, args=(quantiles, 'Frequency', False))
features['MonetaryScore'] = features['Monetary_Total'].apply(rfm_score, args=(quantiles, 'Monetary_Total', False))