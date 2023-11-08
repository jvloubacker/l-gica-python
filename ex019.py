import random
n1 = str(input('Escreva o primeiro nome: '))
n2 = str(input('Escreva o segundo nome: '))
n3 = str(input('Escreva o terceiro nome: '))
n4 = str(input('Escreva o quarto nome: '))
n5 = str(input('Escreva o quinto nome: '))
nomes = [n1, n2, n3, n4, n5] #nomes = ['João Vitor', 'Thomas', 'Erick', 'Samuel', 'Mateus'] ALTERNATIVA JÁ COM OS NOMES
ale = random.choices(nomes)
print(f'O nome sorteado foi {ale}')