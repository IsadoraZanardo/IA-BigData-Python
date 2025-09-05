#QUAL PERÍODO POSSUI MAIS VENDAS (manhã, tarde, noite)
periodo_vendas = X['Period'].value_counts()
print("Período com mais vendas no geral")
periodo_vendas

periodo_vendas.plot(kind='bar', color='green')
plt.ylabel("Número de vendas")
plt.title("Quantidade de vendas por período")
plt.show()