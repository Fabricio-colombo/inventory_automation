import pandas as pd
import time

bebidas = {
    "coca-cola": 5600,
    "pepsi": 4800,
    "guaraná antarctica": 4200,
    "sprite": 900,
    "fanta laranja": 3500,
    "água mineral": 2000,
    "suco de laranja": 3200,
    "chá verde": 1500,
    "café": 1200,
    "chocolate quente": 2500,
    "leite com chocolate": 2800,
    "água de coco": 3000,
    "mate com limão": 2400,
    "limonada": 2700,
    "cerveja pilsen": 5000,
    "vinho tinto": 6400,
    "vinho branco": 6200,
    "vodca": 7000,
    "rum": 6800,
    "whisky escocês": 7500,
    "tequila": 7800,
    "caipirinha": 4200,
    "mojito": 4500,
    "martini seco": 5200,
    "soda italiana": 3800,
    "água tônica": 3500,
    "cerveja artesanal IPA": 5800,
    "champanhe": 6900,
    "sake": 5400,
    "água com gás": 2800
}

for produto, quantidade in bebidas.items():
    if quantidade < 1000:
        print(f"O produto {produto} está abaixo do nível do estoque, com a quantidade de {quantidade} unidades.")
        time.sleep(1)