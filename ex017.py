from math import sqrt
oposto = float(input('Escreva o valor do cateto oposto: '))
adjacente = float(input('Escreva o valor do cateto adjacente: '))

hip= (oposto**2 + adjacente**2)
hip2= sqrt(hip)

print(f"O valor do comprimento da hipotenusa é {hip2:.2f}")