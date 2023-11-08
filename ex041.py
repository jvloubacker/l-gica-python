from datetime import date
atual = date.today().year
nasc = int(input('Digite o seu ano de nascimento: '))
idade = atual - nasc
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print(f'Sua categoria é MIRIM!')

elif idade <= 14:
    print(f'Sua categoria é INFANTIL!')

elif idade <= 19:
    print(f'Sua categoria é JÚNIOR!')

elif idade <= 25:
    print(f'Sua categoria é SÊNIOR!')
else:
    print(f'Sua categoria é MASTER!')
