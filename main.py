# MAIN

from Modulos.ads import carregar_arquivo, calcular_valor_maximo, calcular_valor_minimo, agrupar_categoria, calcular_media, apresentador
from Modulos.auxiliares import temporizador, cabecalho

lista_vendas = carregar_arquivo('vendas.csv')
agrupamento = agrupar_categoria(lista_vendas)


temporizador('INICIANDO O SISTEMA','.', 0.8, 3)
cabecalho('SISTEMA DE ANÁLISE DE DADOS','-', 50)

cabecalho('CATEGORIAS ELENCADAS', '-', 50)
for indice, categoria in enumerate(agrupamento):
    print(f'{indice+1} - {categoria}')

for categoria in agrupamento:
    temporizador('CARREGANDO DADOS:\n',loading='_', tempo=0.4, periodo=5)
    apresentador(f'ESTATÍSTICAS - {categoria.upper()}', agrupamento, categoria)

cabecalho('ESTATÍSTICAS GERAIS', '-', 50)

media = calcular_media(lista_vendas)
val_max = calcular_valor_maximo(lista_vendas)
val_min = calcular_valor_minimo(lista_vendas)

print(f'1 - Preço médio geral: {media}')
print(f'2 - Preço máximo geral: {val_max}')
print(f'3 - Preço mínimo geral: {val_min}')