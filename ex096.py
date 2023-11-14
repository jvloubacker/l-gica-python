# FUNÇÃO 1, TUDO DENTRO DA FUNÇÃO (MAIS PRATICO KK)
def area():
    print('CONTROLE DE AREA')
    print('-'*21)
    lar = float(input('LARGURA (m): '))
    comp = float(input('COMPRIMENTO (m): '))
    print(f'A area de {lar}X{comp} é de {lar*comp}m².')


area()

#FUNÇÃO 2, AS VARIAVEIS FORA DA FUNÇÃO.
'''def area(l,c):
    print('CONTROLE DE TERRENO')
    print('-'*21)
    total= l *c
    print(f'A area de um terreno {l}X{c} é de {total}m².')
lar = float(input('largura (m): '))
comp = float(input('Comp (m): '))
area(lar,comp)'''
