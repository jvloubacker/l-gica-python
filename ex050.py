s = 0
cont = 0
for par in range(1, 7):
    n1 = int(input(f'Digite o {par}ª número: '))
    if n1 % 2 == 0:
        s += n1
        cont+= 1
print(f'Você informou {cont} pares e a soma entre eles são {s}')

