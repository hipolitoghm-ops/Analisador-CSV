# ANALISADOR CSV

Este sistema serve para fazer uma análise de arquivos .csv, a fim
de fazer uma análise dos dados apanhados.

## Funcionalidades

- Criar um dicionário de listas, onde cada lista é referente a uma categoria existente no csv
- Calcular o preço médio, mínimo e máximo de cada categoria
- Apresentar os dados retirados do CSV de forma simples e de fácil entendimento

## Como rodar

1. Ter Python 3.10 instalado
2. Abrir o terminal e seguir para a raiz do projeto
3. No terminal, digitar 'python main.py'

## Estrutura do projeto

- `main.py` — Lê os dados disponibilizados pelo CSV tratado e analisa-os, para que em seguida apresente suas estatísticas
- `Modulos` — Pasta que contém os módulos utilizados pelo arquivo main.py, para o bom funcionamento do projeto
- `Modulos\ads.py` — Módulo voltado para definir as funções principais de análise de dados do projeto
- `Modulos\auxiliares.py` — Módulo voltado para definir as funções auxiliares/cosméticos que ajudam na formatação do projeto 

## Exemplo de saída

```
--------------------------------------------------
           ESTATÍSTICAS - CLASSE GERAL            
--------------------------------------------------
1 - Preço médio da categoria: 12.76
2 - Preço máximo da categoria: 45.0
3 - Preço mínimo da categoria: 1.2
```
## Sobre o projeto

Apesar de ser um projeto simples de análise e tratamento de dados, foi de grande aprendizado
para um contato inicial de como lidar com as informações de um arquivo CSV e como tratá-las.

## Autor

Gabriel Hipólito — [@hipolitoghm-ops](https://github.com/hipolito)