#DADOS ENTRADA (X)
#DADOS SAÍDA (Y)
X = features[['Recency', 'Frequency', 'Monetary_Total', 'Monetary_Average',
              'Variety', 'Country']]
y = features['Champions']


#eSEPARAR TREINO X TESTE
X_train, X_test, y_train, y_test = train_test_split(X, y,
                          test_size=0.3, random_state=42, stratify=y)


#NORMALIZAÇÃO
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)