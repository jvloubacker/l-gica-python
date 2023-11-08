from datetime import date
print('-=-' * 15)
print('Analisador de Anos bisexto')
print('-=-' * 15)
ano = int(input('Qual ano quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(f'O ano {ano} é BISEXTO! ')
else:
    print(f'O ano {ano} NÃO é BISEXTO! ')
