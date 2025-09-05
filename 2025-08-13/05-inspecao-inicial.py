# Inspeção inicial no dataset
print("Dimensão do dataset: ", X.shape)
print("--------------\n")

print("Tipo dos dados")
print(X.dtypes)
print("--------------\n")

print("Valores ausentes")
print(X.isnull().sum())