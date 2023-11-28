from random import randint
from time import  sleep
numeros = list()

def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ',end='')
    for v in range(0,5):
        sort = randint(0, 10)
        numeros.append(sort)
        print(sort, end=' ')
        sleep(0.3)
    print('PRONTO!', end='')

def somaPar(lista):
    soma = 0
    print(f'\nSomando os valores pares de {numeros}, temos ',end='')
    sleep(0.3)
    for par in numeros:
        if par % 2 == 0:
            soma+=par
    print(soma,end='')
    sleep(0.4)


# SISTEMA PRINCIPAL
sorteia(numeros)
somaPar(numeros)
