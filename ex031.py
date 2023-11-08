viagem = int(input('Digite a distância que você vai percorrer em KM: '))

if viagem <= 200:
    preço = viagem * 0.50
    print(f'Você vai pagar {preço} reais na passagem!')

else:
    preço_menor = viagem * 0.45
    print(f'Você vai pagar apenas {preço_menor} reais na passagem!')