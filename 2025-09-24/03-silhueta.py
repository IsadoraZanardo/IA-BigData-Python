from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

inercia = []
silhueta_scores= []

for k in range(2, 10):
  kmeans = KMeans(n_clusters=k, random_state=42,n_init=10)
  kmeans.fit(X_scaled)
  inercia.append(kmeans.inertia_) #inércia é somatória da distância do centroide, método COTOVELO
  score = silhouette_score(X_scaled, kmeans.labels_)
  silhueta_scores.append(score)
#só tem como calcular a distância separando em clusters


#PLOTAR GRÁFICO
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(range(2,10), inercia, marker="o")
plt.title("Método do cotovelo")
plt.xlabel("Clusters")
plt.ylabel("Inércia")

plt.subplot(1,2,2)
plt.plot(range(2,10), silhueta_scores, marker="o")
plt.title("Método da Silhueta")
plt.xlabel("Clusters")
plt.ylabel("Coeficiente")

plt.show()