print('-=-'*9)
print('      GERADOR DE PA')
print('-=-'*9)
primeiro = int(input("DIGITE O PRIMEIRO TERMO: "))
razao = int(input("DIGITE A RAZÃO: "))
termo = primeiro
cont = 1
while cont < 10:
    print(termo, end=' → ')
    termo += razao
    cont += 1
print('FIM')
