# MÓDULO FUNÇÕES AUXILIARES

from time import sleep

def cabecalho(msg,caractere_especial,tamanho = 42):
    print('\n')
    print(f'{caractere_especial}'*tamanho)
    print(f'{msg.center(tamanho)}')
    print(f'{caractere_especial}'*tamanho)
    
def temporizador(msg='', loading='.', tempo=0.5, periodo=3):
    print('\n')
    print(msg, end='')
    sleep(tempo)
    for t in range(0, periodo):
        print(loading, end='')
        sleep(tempo)
    print('\n')
