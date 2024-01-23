ficha = dict()
lista = list()
cont = media = soma = 0
while True:
    ficha['nome'] = str(input('Nome: '))
    cont+=1
    while True:
        ficha['sexo'] = str(input('Sexo: ')).upper()
        if ficha['sexo'] in 'MF':
            break
        print('DIGITE APENAS M  OU F')
    ficha['idade'] = int(input('Idade: '))
    soma+=ficha['idade']
    lista.append(ficha.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0].capitalize()
        if resp in 'SN':
            break
        print('RESPONDA APENAS SIM OU NÃO!!')
    if resp == 'N':
        break

print(f'A) Total cadastradas {cont}.')
media = soma / cont
print(f'B) A média de idade é {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for c in lista:
    if c["sexo"] == 'F':
        print(f'{c["nome"]}')
print('D) Lista das pessoas que estão acima da méida: ')
for p in lista:
    if p["idade"] > media:
        print(f'nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]}')
print("ENCERRADO!")