dic = dict()


def notas(*num,sit=False):
    """
    :param num: uma ou mais notas (aceita varias)
    :param sit: situação do aluno na media(RUIM,RAZOAVEL, BOA)
    :return: dicionario com varias informações dos alunos
    """
    dic['total'] = len(num)
    dic['maior'] = max(num)
    dic['menor'] = min(num)
    soma = 0
    for c in num:
        soma+=c
    dic['media'] = soma / len(num)
    if sit:
        if dic['media'] < 6:
            dic['situação'] = "RUIM"
        elif dic['media'] >=8:
            dic['situação'] = "BOA"
        else:
            dic['situação'] = "RAZOAVEL"
    return dic


# programa principal
resp = notas(9,6,7,10, sit=True)
help(notas)
