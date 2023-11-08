frase = str(input('Escreva uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letras in range(len(junto) - 1, -1, -1):
    inverso += junto[letras]
    print(junto, inverso)
"""if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo')"""
