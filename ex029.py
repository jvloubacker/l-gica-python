velocidade=int(input('Qual foi a velocidade do seu carro? '))

if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade-80)*7
    print(f'Você vai pagar {multa} reais de multa!')

else:
    print('Parabéns por dirigir na velocidade permitida! ')

