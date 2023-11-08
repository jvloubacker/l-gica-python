cont = soma = cont1 = cont2 = 0
while True:
    idade = int(input("Digite sua idade: "))
    if idade > 18:
        cont +=1
    sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]
    if sexo == 'M':
        cont1+=1
    elif sexo == 'F':
        if idade < 20:
            cont2+=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar: [S/N]")).upper().strip()[0]
    if resp == 'N':
        break

print(f"Tem {cont} pessoas que são maiores de 18 anos.")
print(f"Foram {cont1} homens cadastrados.")
print(f"Existe {cont2} mulheres com menos de 20 anos.")


