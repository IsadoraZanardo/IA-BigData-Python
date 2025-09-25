import pandas as pd
import requests

url = "https://github.com/profAndreSouza/Material/blob/main/Intelig%C3%AAncia%20Artificial%20e%20Big%20Data/Datasets/clientes_segmentados.xlsx?raw=true"
response = requests.get(url)

# Salva a planilha em arquivos aqui no colab
with open("clientes_segmentados.xlsx", "wb") as f:
    f.write(response.content)

df = pd.read_excel("clientes_segmentados.xlsx")
display(df.head())

#K É SEMPRE O NÚMERO DE CLUSTERS