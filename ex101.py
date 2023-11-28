def cont(i, f, p):
    """

    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    contador menor do que o final
    """
    cont = i
    while cont <= f:
        print(cont,end=' ')
        cont+=p
    print('FIM')


help(cont)
