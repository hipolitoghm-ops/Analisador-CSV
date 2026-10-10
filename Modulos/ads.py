# MÓDULO FUNÇÕES PRINCIPAIS

import csv
from Modulos.auxiliares import cabecalho

#0. Padronizar dados no CSV
"""
1 - Nome do produto
2 - PN
3 - SN
4- CFF
5 - Preço
6 - Categoria
7- Lote (Se tiver)
8 - Validade (Se tiver lote)
"""

#1. ler arquivo CSV
def carregar_arquivo(arquivo):
    lista_produtos = []
    with open(arquivo, newline='', encoding='utf-8') as csvfile:
        aqv = csv.reader(csvfile)
        for n_linha, linha in enumerate(aqv):
            if n_linha == 0:
                continue
#2. Transformar cada linha em tupla
            lista_produtos.append(tuple(linha))
            
    return lista_produtos
            
#3. Calcular média
def calcular_media(lista_produtos):
    somatorio = 0
    for tupla in lista_produtos:
        numero = float(tupla[4])
        somatorio += numero
    media = somatorio/len(lista_produtos)
    return round(media,2)

#3.1. Calcular valor máximo
def calcular_valor_maximo(lista_produtos):
    valor_maximo = 0
    for indice, linha in enumerate(lista_produtos):
        valor = linha[4]
        valor = float(valor)
        if indice == 0:
            valor_maximo = valor
        elif valor > valor_maximo:
            valor_maximo = valor
    return valor_maximo

#3.2. Calcular valor mínimo
def calcular_valor_minimo(lista_produtos):
    valor_minimo = 0
    for indice, linha in enumerate(lista_produtos):
        valor = float(linha[4])
        if indice == 0 or valor < valor_minimo:
            valor_minimo = valor
    return valor_minimo
    
#4. Agrupar por categoria usando dicionário
def agrupar_categoria(lista_produtos):
    agrupamento = {}
    for linha in lista_produtos:
        categoria = linha[5]
        if categoria not in agrupamento:
            agrupamento[categoria] = []
        agrupamento[categoria].append(linha)

    return agrupamento


def apresentador(titulo, agrupamento, categoria):
    cabecalho(titulo, '-', 50)
    produto = agrupamento[categoria]
    media = calcular_media(produto)
    val_max = calcular_valor_maximo(produto)
    val_min = calcular_valor_minimo(produto)

    print(f'1 - Preço médio da categoria: {media}')
    print(f'2 - Preço máximo da categoria: {val_max}')
    print(f'3 - Preço mínimo da categoria: {val_min}')