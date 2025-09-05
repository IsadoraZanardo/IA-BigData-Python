#PERÍODO (manhã, tarde, noite) QUE O CLIENTE QUE MAIS COMPROU COSTUMA COMPRAR

#FILTRAR TANSAÇÕES DESSE CLIENTE
transacoes_cliente = X[X['CustomerID'] == cliente_id]
periodo_cliente = transacoes_cliente['Period'].value_counts()
print(f"\nPeríodo em que o cliente {cliente_id} mais compra:")
print(periodo_cliente)