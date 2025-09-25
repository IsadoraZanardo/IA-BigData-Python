k = 4 #número de clusters
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10) #"n_init" roda o algoritmo 10 vezes com diferentes centroides iniciais e escolhe o melhor
df["cluster_r"] = kmeans.fit_predict(X_scaled)

df[["idade", "cluster_r"]].head()

#K É SEMPRE O NÚMERO DE CLUSTERS
#começa sempre no zero