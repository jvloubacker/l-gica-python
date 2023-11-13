from time import sleep
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    cont = 0
    while i <= f:
        print(cont)
        cont+=1


contador(1, 10, 1)
