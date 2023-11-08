r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
equilatero = r1 == r2 == r3
isósceles = r1 == r2 != r3 or r1 == r3 != r2 or r3 == r2 != r1
escaleno = r1 != r2 != r3 != r1
triangulo = r1 + r2 > r3 or r2 + r1 > r2 or r3 + r1 > r2
if triangulo == equilatero:
    print('Podem formar um triângulo EQUILÁTERO!')
elif triangulo == isósceles:
    print('Podem formar um triângulo ISÓSCELES!')
elif triangulo == True and triangulo == escaleno:
    print('Podem formar um triângulo ESCALENO!')
else:
    print('NÃO podem formar um triângulo!')