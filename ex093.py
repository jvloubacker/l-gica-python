ficha = dict()
partidas = list()

ficha['nome'] = str(input('Nome do jogador: '))
part = int(input(f'Quantas partidas {ficha["nome"]} jogou? '))
for c in range(part):
    partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
    ficha['gols'] = partidas[:]
    ficha['total'] = sum(partidas)
print('-='* 20)
print(ficha)
print('-='*20)
for k,v in ficha.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {ficha["nome"]} jogou {part} partidas.')
for c, n in enumerate(ficha['gols']):
    print(f'    => Na partida {c}, fez {n} gols.')
print(f'Foi um total de {ficha["total"]}')