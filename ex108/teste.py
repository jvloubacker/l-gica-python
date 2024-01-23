from ex108 import moedas

p = float(input('Digite o preço: R$'))
print(f'O dobro de {moedas.moedas(p)} é {moedas.moedas(moedas.dobro(p))}')
print(f'A metade de {moedas.metade(p)} é {moedas.metade(p)}')
print(f'Aumentando em 10%, temos {moedas.moedas(moedas.aumentar(p,10))}')
print(f'Diminuindo em 13%, temos {moedas.moedas(moedas.diminuir(p,13))}')
