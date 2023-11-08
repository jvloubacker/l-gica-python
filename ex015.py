km = float(input('Quantos km pecorridos? '))
dias = float(input('Por quanto dias ele foi alugado? '))

d = dias * 105.90
k = km * 0.15
total = d + k

print(f'Você vai pagar R${total} pelo alguel do carro!')