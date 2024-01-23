def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um valor inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31m\nENTRADA DE DADOS INTERROMPIDA PELO O USUARIO.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg=0):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um valor real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31m\nENTRADA DE DADOS DO USUARIO INTERROMPIDA\033[m')
            return 0
        else:
            return n


# PROGRAMA PRINCIPAL
n = leiaInt('Digite um Inteiro: ')
n1 = leiaFloat('Digite um Real: ')
print(f'\033[1;32mO valor inteiro digitado foi {n} e o real foi {n1}.\033[m')
