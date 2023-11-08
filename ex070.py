soma = cont = totalmil = quant = menor = 0
while True:
    produto= str(input("Escreva o nome do produto: "))
    preco = int(input("Digite o preço: "))
    quant+=1
    if quant == 1:
        produto = preco
        menor = produto
    else:
        if preco < menor:
            menor = produto

    soma+=preco
    if preco > 1000:
        cont+=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input("Quer continuar: [S/N] ")).upper().strip()[0]
    if resp == 'N':
        break
print(f"O valor total da compra foi de R${soma} reais.")
print(f"No total existe {cont} produtos mais de R$1.000 reais.")
print(f"O produto mais barato é o {produto}.")
