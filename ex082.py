valor = list()
pares = list()
impares = list()
while True:

    valor.append(int(input('Digite um número: ')))
    resp = str(input("Quer continuar: [S/N] ")).upper().capitalize()[0]
    if resp == 'N':
        break
for pos, v in enumerate(valor):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2== 1:
        impares.append(v)

print(f'Os valores adicionados foram esses {valor}')
print(f"Os valores impares são esses {impares}")
print(f"Os valores pares são esses {pares}")