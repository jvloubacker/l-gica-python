casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o seu salário atual do comprador: R$"))
anos = int(input("Em quantos anos você quer pagar a casa? "))
prestação = casa /(anos * 12)
minimo = 30 / 100 * salario

print(f"Para pagar a casa de R${casa} reais em {anos} anos, a prestação sera de R${prestação:.2f} reais por mês!")

if prestação <= minimo:
    print(f"Empréstimo Concedido!")

else:
    print(f"Empréstimo Negado")
