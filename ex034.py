salario = float(input('Digite o seu salario: '))
if salario <= 1250:
    porcento = ('15%')
    novo = salario + (salario * 15 / 100)
else:
    porcento = ('10%')
    novo = salario + (salario * 10 / 100)

print(f'Você recebeu um aumento de {porcento}, seu novo salário é {novo}!')