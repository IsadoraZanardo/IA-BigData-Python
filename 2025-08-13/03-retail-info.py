from ucimlrepo import fetch_ucirepo

#FETCH DATASET
online_retail = fetch_ucirepo(id=352)

#DATA (aandas dataframe)
X = online_retail.data.features
y = online_retail.data.targets

#METADATA
print(online_retail.metadata)

#VARIABLE INFORMATION
print(online_retail.variables)