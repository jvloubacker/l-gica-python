lista = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}ª número: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Todos os números digitados: {lista}')
print(f'Todos os numeros pares em ordem : {lista[0]} ')
print(f'Todos os numeros imapres em ordem : {lista[1]}')
