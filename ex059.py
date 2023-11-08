from time import sleep
v1 = int(input('Digite o primeiro número: '))
v2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('''DIGITE SUA OPÇÃO ABAIXO:
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    opcao = int(input("\033[01;31mDigite sua opção:\033[m "))
    if opcao == 1:
        soma = v1 + v2
        print(f"A soma entre {v1} + {v2} = {soma}")
    elif opcao == 2:
        multi = v1 * v2
        print(f"A multi entre {v1} * {v2} = {multi}")
    elif opcao == 3:
        if v1 > v2:
            maior = v1
        elif v2 > v1:
            maior = v2
            print(f"O maior entre {v1} e {v2} é {maior}")
        else:
            igual = v1 == v2
            print(f'Os números {v1} e {v2} são iguais')

    elif opcao == 4:
        v1 = int(input("Primeiro valor: "))
        v2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Você finalizou o programa!")
    else:
        print("Opção Inválida, TENTE NOVAMENTE...")
    sleep(0)
print('Acabou!')



