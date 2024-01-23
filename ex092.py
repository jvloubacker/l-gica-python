import datetime
ct = dict()
ct['nome'] = str(input('Digite o seu nome: '))
ano = int(input('Ano de nascimento: '))
ct['idade'] = datetime.datetime.now().year - ano
ct['CT'] = int(input('CT (0 não tem): '))
if ct['CT'] != 0:
    ct['contratação'] = int(input('Ano da contratação: '))
    ct['salario'] = float(input('Salario: R$'))
    ct['aposentadoria'] = ct['idade'] + ((ct['contratação'] + 35) - datetime.datetime.now().year)
print('-='*20)
for k, v in ct.items():
    print(f'    - {k} tem o valor {v}')
