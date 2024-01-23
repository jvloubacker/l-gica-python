def fatorial(n,show=False):
    """

    :param n: o numero a ser calculado
    :param show: parametro (opcional), mostrar a conta
    :return: o valor fatorial de um numero n
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c,end='')
            if c>1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f*=c
    return f


#programa principal
print('-'*25)
print(fatorial(5, show=False))