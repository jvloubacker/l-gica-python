primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro + (11 - 1) * razao
while primeiro < termo:
    primeiro += razao
    print(primeiro, end='')
    print(f' → ' if primeiro > 0 else 'FIM', end='')
print('FIM')
