from random import randint
from time import sleep

def sorteia(lista):
    for c in range(0, 5):
        lista.append(randint(1,10))
    print(f'Sorteando 5 valores da lista: {lista} PRONTO!')



def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma+=valor
    print(f'Os valores somados pares {lista} deu, {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)