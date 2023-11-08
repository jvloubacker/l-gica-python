from random import randint
from time import sleep
from operator import itemgetter
dado = {'Jogador1': randint(1,6),
        'Jogador2': randint(1,6),
        'Jogador3': randint(1,6),
        'Jogador4': randint(1,6)}
ranking = list()
print('Valores sorteados:')
for k, v in dado.items():
        print(f'{k} tirou {v} no dado.')
        sleep(1)
print('-='*20)
ranking = sorted(dado.items(), key= itemgetter(1), reverse=True)
print("  ==RANKING DOS JOGADORES==")
for c, i in enumerate(ranking):
        print(f'  {c+1}º lugar: {i[0]} com {i[1]}')
        sleep(1)
print('  JOGO FINALIZADO!')