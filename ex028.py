from random import randint
from time import sleep
sortear= randint(0,5)
print('-=-'*20)
print('Vou pensar em um número entre 0 a 5. TENTE DESCOBRIR! ')
print('-=-'*20)
jogador = int(input('Escreva um número para adivinhar: '))
print('PROCESSANDO...')
sleep(2)
if jogador == sortear:
    print('Parabéns,você acertou, vai ganhar uma Ferrari!')

else:
    print(f'Você errou, seu mlk, o número que eu tinha pensado era o {sortear}')
