tot = 0
n = int(input('Digite um número: '))
for np in range(1, n + 1):
    if n % np == 0:
        print('\033[033m', end =' ')
        tot+=1
    else:
        print('\033[035m', end=' ')
    print(np)
print(f'\033[mO número {n} foi divisivel {tot} vezes')
if tot == 2:
    print('Por isso ele é primo.')
else:
    print('Ele não é primo')