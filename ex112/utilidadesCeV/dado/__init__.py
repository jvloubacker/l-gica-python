def leiaDinheiro(msg):
    valido = False
    while not valido:
        n = str(input(msg)).replace(',','.')
        if n.isalpha() or n.strip() == '':
            print(f'\033[1;31mERRO! \"{n}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(n)