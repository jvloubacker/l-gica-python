compra = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] á vista no dinheiro
[2] á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção de pagamento? '))
dinheiro = compra - (10 / 100 * compra)
avcartão = compra - (5/ 100 * compra)
compra2 = compra / 2
#compra3 = (20/100 * compra) + compra
#parc = compra3 / parcela
if opção == 1:
    print(f'Sua compra de R${compra} vai para R${dinheiro} no final.')
elif opção == 2:
    print(f'Você recebeu 5% de desconto')
    print(f'Sua compra de R${compra} vai para R${avcartão} á vista no cartão.')
elif opção == 3:
    print(f'2x no cartão não tem desconto!')
    print(f'Sua parcela será 2x de {compra2}.')
elif opção == 4:
    parcela = int(input('Quantas parcelas vão ser? '))
    compra3 = (20 / 100 * compra) + compra
    parc = compra3 / parcela
    print(f'Sua compra será parcelada em {parcela}x de {parc} COM JUROS.')
    print(f'Sua compra de {compra} vai para {compra3} no final.')