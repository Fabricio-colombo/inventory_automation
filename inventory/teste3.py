import pymongo
import pandas as pd
import time

# Conexão com o MongoDB
conexao_string = "mongodb://localhost:27017"
client = pymongo.MongoClient(conexao_string)

db = client["Produtos_Estoque"]
collection = db["Bebidas"]

# Lendo os dados do MongoDB e armazenando em um DataFrame
bebidas = pd.DataFrame(list(collection.find()))

# Dicionário para armazenar produtos abaixo do nível de estoque
produtos_abaixo_estoque = {}

# Iterar sobre as colunas do DataFrame
for coluna in bebidas.columns:
    produto = coluna  # O nome do produto é a própria coluna
    quantidade = bebidas[coluna][0]  # A quantidade em estoque é obtida do primeiro (e único) valor na coluna

    if quantidade < 1000:
        produtos_abaixo_estoque[produto] = quantidade

# Fechando a conexão com o MongoDB
client.close()

# Imprimindo os produtos abaixo do nível de estoque
for produto, quantidade in produtos_abaixo_estoque.items():
    print(f"O produto {produto} está abaixo do nível do estoque, com a quantidade de {quantidade} unidades.")
    time.sleep(1)
