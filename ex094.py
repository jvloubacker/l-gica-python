pessoa = dict()
dados = list()
cont = 0
media = 0
while True:
    pessoa['nome'] = str(input("Nome: "))
    cont += 1
    while True:
        pessoa['sexo'] = str(input("Sexo: ")).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("ERRO! DIGITE APENAS M[MASCULINO] OU F[FEMININO]")
    pessoa['idade'] = int(input("Idade: "))
    media += pessoa['idade']
    media1 = media / cont
    dados.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! RESPONDA APENAS SIM NÃO.')
    if resp == 'N':
        break
print('-=' * 20)
print(dados)
print('-=' * 20)
print(f'A) Ao todo temos {cont} pessoas cadastradas.')
print(f'B) A média de idade é de {media1:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in dados:
    if p['sexo'] in "Ff":
        print(f'{p["nome"]}', end=' ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in dados:
    if p['idade'] >= media1:
        print(f'   ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print("ENCERRADO!")
