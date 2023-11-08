from random import randint
from time import sleep
jogadortent = 0
ale = randint(1, 10)
print('PROCESSANDO...')
sleep(2)
#print(f'O computador pensou no número {ale}.')
jogador = int(input('Pense em número de 1 a 10: '))
if jogador == ale:
    print('Parabens voce ganhou!')
else:
    if jogador < ale:
        print("Mais... Tente novamente")
    elif jogador > ale:
        print("Menos... Tente novamente.")
while jogador != ale:
    jogador = int(input('Pense em número de 1 a 10: '))
    jogadortent+=1
    if jogador == ale:
        print('Parabens voce ganhou!')
    else:
        if jogador < ale:
            print("Mais... Tente novamente")
        elif jogador > ale:
            print("Menos... Tente novamente.")
print(f'Você acertou finalmente, depois de {jogadortent} tentativas.')