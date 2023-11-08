import datetime
ct = dict()
ct['nome'] = str(input("Nome: "))
ano= int(input("Ano de nascimento: "))
ct['idade'] = datetime.datetime.now().year - ano
ct['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if ct['ctps'] != 0:
    ct['contratação'] = int(input('Ano de contratação: '))
    ct['salario'] = float(input("Salário: R$ "))
    ct['aposentadoria'] = ct['idade']+ (ct['contratação'] + 35) - datetime.datetime.now().year
print('-='*20)
print(ct)
for k,v in ct.items():
    print(f'{k} tem o valor {v}')
