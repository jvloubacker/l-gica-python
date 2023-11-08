from math import hypot
oposto = float(input('Escreva o valor do cateto oposto: '))
adjacente = float(input('Escreva o valor do cateto adjacente: '))
hi = hypot(oposto, adjacente)
print(f"A hipotenusa vai medir {hi:.2f}")