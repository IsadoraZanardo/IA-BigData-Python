#VALOR TOTAL POR PAÍS
X['Total'] = X['Quantity'] * X['UnitPrice']
vendas_pais = X.groupby('Country')['Total'].sum().sort_values(ascending=False).head(10)
print("Vendas por país:")
print(vendas_pais)

#PLOT VENDAS X PAÍS
sns.barplot(x=vendas_pais.index, y=vendas_pais.values)
plt.title("Valor Total por País")
plt.xticks(rotation=45)
plt.show()