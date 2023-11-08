valores = list()
while True:
    num = int(input("Digite um número: "))
    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso')
    else:
        print('VALOR DUPLICADO. TENTE NOVAMNTE')
    resp = str(input("Quer continuar: [S/N] ")).upper().capitalize()[0]
    if resp == 'N':
        break
valores.sort()
print(f"Os valores adicionados em forma crescente {valores}")