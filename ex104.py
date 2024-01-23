def LeiaInt(num):
    valor = 0
    ok = False
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;32mEERRO! APENAS NÚMEROS!\033[m')
        if ok:
            break
    return valor

# programa principal
n = LeiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')