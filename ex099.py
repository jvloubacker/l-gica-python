def maior(*num):
    maior= 0
    cont = 0
    print('-='*20)
    print('Analisando os valores passados')
    for m in num:
        print(f'{m}',end=' ')
        cont+=1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')



# programa principal
maior(5, 7, 9, 5)
maior(5, 1, 0)
maior(8, 2)
maior(1)
maior(0)
