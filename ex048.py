soma = 0
cont = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont+= 1
        soma= soma + c

print(f"A soma de todos os {cont} valores é {soma}")
#print(c) PARA SABER O QUE A VAR C FAZ

