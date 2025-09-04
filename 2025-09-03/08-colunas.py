#COLUNA RFM
features['RFM_Score'] = (
    features['RecencyScore'].astype(str) +
    features['FrequencyScore'].astype(str) +
    features['MonetaryScore'].astype(str)
)


#COLUNA ALVO
features['Champions'] = (features['RFM_Score'] == '444').astype(int)

features