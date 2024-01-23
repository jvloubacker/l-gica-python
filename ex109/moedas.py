def aumentar(num=0, taxa=0, formato=False):
    aum = num + (taxa / 100 * num)
    return aum if formato is False else moedas(aum)


def diminuir(num=0, taxa=0, formato=False):
    dim = num - (taxa / 100 * num)
    return dim if formato is False else moedas(dim)


def dobro(num=0, formato=False):
    dob = num * 2
    return dob if formato is False else moedas(dob)


def metade(num=0, formato=False):
    met = num / 2
    return met if formato is False else moedas(met)


def moedas(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
