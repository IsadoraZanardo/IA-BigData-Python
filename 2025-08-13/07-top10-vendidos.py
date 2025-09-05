#ANÁLISE EXPLORATÓRIA

#TOP 10 PRODUTOS MAIS VENDIDOS
top_produtos = X.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 produtos mais vendidos:")
print(top_produtos)