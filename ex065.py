resp = 'S'
quant = soma = media = maior = menor =0

while resp in "Ss":
    num = int(input("Digite um número: "))
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
    soma+= num
    quant+=1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media+= soma / quant
print(f"Você digitou {quant} números e a média foi de {media:.2f}")
print(f"O maior valor foi de {maior} e o menor foi {menor}")