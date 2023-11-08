medidade = 0
maioridadehom = 0
nome_vlh = ""
totmulhernova = 0
for p in range(1, 5):
    print('-' * 6, f'{p}ª PESSOA', '-' * 6)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sx = str(input("Sexo [M/F]: ")).strip()
    medidade += idade / 4
    if p == 1 and sx in 'Mm':
        maioridadehom = idade
        nome_vlh = nome
    if sx in 'Mm' and idade > maioridadehom:
        maioridadehom = idade
        nome_vlh = nome
    if idade <= 20 and sx in 'Ff':
        totmulhernova += 1


print(f'A média dde idade do grupo é {medidade} anos.')
print(f'O homem mais velho tem {maioridadehom} anos e nome é {nome_vlh}.')
print(f'Ao todo são {totmulhernova} mulheres com menos de 20 anos.')
