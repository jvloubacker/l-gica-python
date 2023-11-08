from math import factorial
num = int(input("Vamos fatorar: "))
f = factorial(num)
print(f"O fatorial de {num}! é {f}")
c = num
while c > 0:
    c -= 1
    print(f"{c+1}", end='')
    print(f' x ' if c > 0 else ' = ', end='')
print(f'{f}', end='')