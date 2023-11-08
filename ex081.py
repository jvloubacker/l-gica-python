lista = list()
cont = 0
while True:

    num = lista.append(int(input('Digite um número: ')))
    if num in lista:
        lista.remove(2)
    cont+=1

    resp = str(input('Você quer continuar: [S/N] ')).upper().capitalize()[0]
    if resp == 'N':
        break


print(f'O total de números digitados foram {cont}')
lista.sort(reverse=True)
print(f'Os valores descrecente são {lista}')
if 5 in lista:
    print(f'O número 5 esta na lista.')
else:
    print(f"O número 5 nao esta na lista.")