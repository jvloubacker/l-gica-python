print('-'*30)
print(f"{'LISTAGEM DE PREÇOS':^30}")
print('-'*30)
listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
for pos in range (len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}R$",end=' ')
    else:
        print(f"{listagem[pos]:.2f}")