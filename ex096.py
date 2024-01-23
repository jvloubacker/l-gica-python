def area(larg, comp):
    print('CONTROLE DE TERRENOS')
    print('-'*20)
    a = larg  * comp
    print(f'A area total é de {a} metros quadrados.')
    
# PROGRAMA PRINCIPAL
l = float(input('Digite a largura: '))
c = float(input('Digite o comprimento em metros: '))
area(l, c)