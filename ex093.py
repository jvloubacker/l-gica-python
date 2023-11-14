jogador = dict()
partidas = list()
totgols = 0
jogador['nome'] = str(input("Digite o nome do jogador: "))
part = int(input(f"Quantas partidas o {jogador['nome']} jogou? "))
for c in range(0, part):
    partidas.append(int(input(f"Quantos gols ele fez na partida {c}: ")))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*20)
print(jogador)
print('-='*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {jogador["nome"]} jogou {part} partidas.')
for i, v in enumerate(jogador["gols"]):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]}')