temp = list()
princi = list()
maior = menor = 0
cont = 0
while True:
    temp.append(str(input('Nome: ')))
    cont +=1
    temp.append(float(input('Peso: ')))
    if len(princi) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = [1]
    princi.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar: [S/N] ')).capitalize()[0]
    if resp in 'Nn':
        break

print(f'Ao todo, foram {cont} pessoas cadastradas.')
print(f'O maior peso é de {maior}Kg. Peso de ' , end='')
for p in princi:
    if p[1] == maior:
        print(f'[{p[0]}] ',end='')
print('')
print(f'O menor peso é {menor}Kg. Peso de ',end='')
for c in princi:
    if c[1] == menor:
        print(f'[{c[0]}]', end='')
