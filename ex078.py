valor = list()
for c in range(0, 5):
    valor.append(int(input(f"Digite um valor para posição {c}: ")))
print(f'Os valores digitados foram {valor}.')
print(f'O menor valor digitado foi {min(valor)}. posição', end='')
for pos, v in enumerate(valor):
    if min(valor) == v:
        print(f' {pos}...', end='')
print(f"\nO maior valor digitado foi {max(valor)}. posição", end='')
for pos, v in enumerate(valor):
    if max(valor) == v:
        print(f' {pos}...', end='')

