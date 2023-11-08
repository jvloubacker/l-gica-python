num = int(input('Digite um número: '))
print(''' Escolha umas das bases para conversão
[1] para binário
[2] Para Octal
[3] Para HEXADECIMAL ''')
opção = int(input('Escolha uma opção para conversão: '))

if opção == 1:
    print(f'{num} convertido para BINÁRIO é {bin(num)[2:]}!')

elif opção == 2:
    print(f"{num} convertido para OCTAL é {oct(num)[2:]}!")

elif opção == 3:
    print(f"{num} Convertido para Hexadecimal é {hex(num)[2:]}")

else:
    print("Opção inválida. Tente outro opção! ")