print("BEM VINDO A ANALISE DE DADOS")
print("-=" * 16)
num = (int(input("Digite o primeiro número: ")),
    int(input("Digite o segundo número: ")),
    int(input("Digite o terceiro número: ")),
    int(input("E o quarto número: ")))
print(f"Você digitou os valores {num}")
print(f"O valor 9 pareceu {num.count(9)} vezes.")
if 3 in num:
    print(f"O valor 3 apareceu na {num.index(3)+1}ª posição.")
else:
    print("Não tem número 3.")
print(f"Os valores pares digitados foram ")
for n in num:
    if n % 2 == 0:
        print(n, end='  ')



