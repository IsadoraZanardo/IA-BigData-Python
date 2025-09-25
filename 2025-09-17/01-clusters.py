#CALCULAR LIMITES
x_min = df['idade'].min()
x_max = df['idade'].max()
y_max = df.groupby('cluster')['idade'].value_counts().max()  #contagem máxima por cluster


#FIGURE E EIXOS 2x2
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()


#ITERAR PELOS CLUSTERS
for i, cluster_id in enumerate(sorted(df['cluster'].unique())):
    sns.histplot(
        data=df[df['cluster'] == cluster_id],
        x="idade",
        bins=20,
        ax=axes[i],
        color=f"C{i}",
    )
    axes[i].set_title(f"Distribuição de Idade - Cluster {cluster_id}")
    axes[i].set_xlabel("Idade")
    axes[i].set_ylabel("Contagem")
    axes[i].set_xlim(x_min, x_max)
    axes[i].set_ylim(0, y_max + 1)

plt.tight_layout()
plt.show()