from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0, 2)
print('''Suas opçôes:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
opc = int(input('Qual é a sua jogada? '))
print('-='* 14)
print(f'O computador escolheu {itens[comp]}')
print(f'O jogador escolheu {itens[opc]}')
print('-='* 14)

if comp == 0:
    if opc == 0:
        print(f'Você empatou!')
    elif opc == 1:
        print(f'Você GANHOU!')
    elif opc == 2:
        print(f'Você PERDEU!')
    else:
        print(f'OPÇÃO INVÁLIDA!')
elif comp == 1:
    if opc == 0:
        print(f'Você PERDEU!')
    elif opc == 1:
        print(f'Você EMPATOU!')
    elif opc == 2:
        print('Você GANHOU!')
    else:
        print(f'OPÇÃO INVÁLIDA!')

elif comp == 2:
    if opc == 0:
        print(f'Você GANHOU!')
    elif opc == 1:
        print(f'Você PERDEU!')
    elif opc == 2:
        print(f'Você EMPATOU!')
    else:
        print(f'OPÇÃO INVÁLIDA!')
