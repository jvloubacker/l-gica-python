def aumentar(num=0, taxa=0):
    aum = num + (taxa / 100 * num)
    return aum


def diminuir(num=0, taxa=0):
    dim = num - (taxa / 100 * num)
    return dim


def dobro(num=0):
    dob = num * 2
    return dob


def metade(num=0):
    met = num / 2
    return met


def moedas(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
