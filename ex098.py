from time import sleep
def contador(i, f, p):
    if p < 0
        p*= -1
    if p == 0
        p =1
    print('-='*20)
    print(f'CONTAGEM DE {i} até {f} de {p} em {p}')
    if i < f:
        cont= i
        while cont <= f:
            print(cont,end=' ')
            sleep(0.5)
            cont+=p
        print('FIM')
    else:
        cont = i
        while cont >=f:
            print(cont,end=' ')
            sleep(0.5)
            cont-=p
        print('FIM')

# programa  principal
contador(0,10,1)
contador(10,0,2)
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)