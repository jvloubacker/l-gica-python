from time import sleep

c = ('\033[m',  # 0 sem cor
     '\033[0;30;41m',  # 1 vermelho
     '\033[7;47m',  # 2 branco
     '\033[0;44m',  # 3 azul
     '\033[42m',  # - Fundo verde
     '\033[43m',  # - Fundo amarelo
     '\033[45m',  # - Fundo magenta
     '\033[46m'  # - Fundo ciano
     )


def ajuda(com):
    titulo(f'ACESSANDO O MANUEL DO COMANDO \'{com}\'', 3)
    print(c[2],end='')
    help(com)
    print(c[0],end='')

def titulo(msg, cor=0):
    sleep(1.5)
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f' {msg}')
    print('~' * tam)
    print(c[0])


# PROGRAMA PRINCIPAL
comando = ''
while True:
    titulo('  SISTEMA DE AJUDA PyHelp', 1)
    sleep(1.8)
    print(c[7],end='')
    comando = str(input('FUNÇÃO OU BIBLIOTECA >>'))
    print(c[0],end='')
    if comando.upper() == 'FIM':
        break
    else:

        ajuda(comando)
titulo('  ATÉ LOGO', 1)
