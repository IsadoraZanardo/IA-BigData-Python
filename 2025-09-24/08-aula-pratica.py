#TAREFA PRÁTICA

#1. Teste diferentes valores de k e observe como os clusters mudam.
#igual 04-k-means.py
k = 2 #NÚMERO DE CLUSTERS
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
df["cluster_r"] = kmeans.fit_predict(X_scaled)
df[["idade", "cluster_r"]].head()



#2. Compare cenários variando as variáveis utilizadas.
#AUMENTANDO CLUSTERS > amostra homogênea
#DIMINUINDO CLUSTERS > amostra heterogênea



#3. Analise os perfils emergentes e proponha estratégias ou ações para cada grupo.
#CLUSTER 0 > mais jovens, menor renda mensal
#CLUSTER 1 > mais velhos, maior renda mensal



#4. Reflita sobre como outliers e escalas diferentes afetam os resultados.
#OULIERS (pontos de dados distantes da maioria dos outros pontos) podem distorcer os clusters
#ESCALAS DIFERENTES garantem maior amplitude nos resultados observados