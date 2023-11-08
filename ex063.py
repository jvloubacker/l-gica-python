print('SEQUENCIA DE FIBONACCI!')
n= int(input('Quantos termos vc quer? '))
t1 = 0
t2 = 1
print(f'{t1} - {t2} - ',end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    t1 = t2 #o t1 vai receber o t2 PARA SOMAR
    t2 = t3 #o t2 vai receber o t3 PARA PODER SOMAR, E ASSIM SUCESSIVAMENTE.
    print(f'{t3} - ',end='')
    cont+=1
print('FIM')