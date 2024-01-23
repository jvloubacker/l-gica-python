ficha = dict()
partidas = list()
time = list()
while True:
    ficha.clear()
    ficha['nome'] = str(input('Nome do jogador: '))
    part = int(input(f'Quantas partidas {ficha["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, part):
        partidas.append(int(input(f'   Quantos gols na partida {c}? ')))
    ficha['gols'] = partidas[:]
    ficha['total'] = sum(partidas)
    time.append(ficha.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().capitalize()[0]
        if resp in 'SN':
            break
        print('ERRO! APENAS SIM OU NÃO!')
    if resp == 'N':
        break
print('-='*20)
print('cod nome          gols         total')
print('-'*40)
for i, n in enumerate(time):
    print(f'{i}  ', end='')
    for d in n.values():
        print(f'{str(d):<16}',end='')
    print()
print('-'*40)
while True:
    resp2= int(input('Mostrar dados de qual jogadodr? (999 para parar)'))
    if resp2 == 999:
        break
    if resp2 >= len(time):
        print(f'ERRO! Não existe jogador com o cod {resp2}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[resp2]["nome"]}!')
        for j, g in enumerate(time[resp2]['gols']):
            print(f'No jogo {j+1} fez {g} gols.')
print('PROGRAMA ENCERRADO!!')