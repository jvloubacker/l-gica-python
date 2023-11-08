peso = float(input('Qual é o seu peso (Kg): '))
altura = float(input('Qual é a sua altura (m): '))
imc = peso / (altura * altura)
print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc <= 18.5:
    print(f'Essa pessoa está ABAIXO DO PESO!')
elif imc <= 25:
    print(f'Você está no PESO IDEAL!')
elif imc <= 30:
    print(f'Você está em SOBREPESO!')
elif imc <= 40:
    print(f'Você está em OBESIDADE!')
else:
    print(f'\033[1;31;40mVocê está com OBESIDADE MÓRBIDA!\033[m')
