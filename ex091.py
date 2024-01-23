from time import sleep
from random import randint
from operator import itemgetter
dados = {'Jogador1': randint(1,6),
         'Jogador2': randint(1,6),
         'Jogador3': randint(1,6),
         'Jogador4': randint(1,6)}
ranking = list()
for k, v in dados.items():
    print(f'{k} {v}')
    sleep(1)
ranking = sorted(dados.items(), key = itemgetter(1),reverse=True)
print('-='*20)
print(' == RANKING DOS JOGADORES ==')
for c, v in enumerate(ranking):
    print(f'    {c+1}º lugar: {v[0]} {v[1]}.')
    sleep(1)