print('=-' * 30)
print(' '*15, 'BEM VINDOS AO BANCO MUNDIAL JV')
print('=-' * 30)
valor = int(input('Qual sera o valor sacado? '))
total = valor
ced = 50
totced = 1
while True:
    if total >= ced:
        total -=ced
        totced+=1
    else:
        if totced > 0:
            print(f'O total de cedulas {totced} e o valor da cedula é {ced}')
        if ced ==50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced=0
        if total == 0:
            break

