import moedas

p = float(input('Digite o preço: R$'))
print(f'O dobro de R${p} é R${moedas.dobro(p)}')
print(f'A metade de R${p} é R${moedas.metade(p)}')
print(f'Aumentando em 10%, temos R${moedas.aumentar(p,10)}')
print(f'Diminuindo em 13%, temos R${moedas.diminuir(p,13)}')
