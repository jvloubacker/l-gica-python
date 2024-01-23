def aumentar(num=0, taxa=0, formato=False):
    """
    => Calcula um determinado aumento no preço,
    retornando o resultado com ou sem formatação no preço.
    :param num: valor a ser aumentado
    :param taxa: taxa de aumento
    :param formato: formatação no preço com virgula(opcional)
    :return: o valor reajustado, com ou sem formatação
    """
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


def resumo(preço=0, taxa1=10, taxa2=20):
    """

    :param preço:
    :param taxa1:
    :param taxa2:
    :return:
    """
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moedas(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxa1}% de aumento: \t{aumentar(preço, taxa1, True)}')
    print(f'{taxa2}% de redução: \t{diminuir(preço, taxa2, True)}')
    print('-' * 30)
