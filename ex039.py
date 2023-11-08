from datetime import date
print('''[1] Homem
[2] Mulher
[3] Outro ''')
opção = int(input('Selecione uma opção: '))
atual = date.today().year
nascimento = int(input('Digite o ano do seu nascimento: '))
idade = atual - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}.')

if opção == 2:
    print(f"Você Mulher não tem a obrigatoriedade de se alistar! ")

elif opção == 3:
    print(f"Não existe outro. Só existe HOMEM E MULHER!")

elif idade == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE!')

elif idade > 18:
    print(f'Seu alistamento foi em {nascimento+18}')
    saldo = idade - 18
    print(f'Você já deveria ter se há alistado a {saldo} anos.')

elif idade < 18:
    saldo = 18 - idade
    print(f'Você ainda não tem 18 anos. Ainda faltam {saldo} anos para se alistar.')
    anos = atual + saldo
    print(f'Seu alistamento será em {anos} anos')
