import pandas as pd
from sklearn.preprocessing import StandardScaler

variaveis = ["idade", "renda_mensal"]
X = df[variaveis]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Original -> Scaled")

for i in range(5):
    print("-"*40)
    for j, var in enumerate(variaveis):
        print(f"{var} = {X.iloc[i,j]:.2f} -> {var}_scaled = {X_scaled[i,j]:.2f}")