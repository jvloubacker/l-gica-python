from random import randint
from time import sleep
soma = 0
print("VAMOS JOGAR PAR OU ÍMPAR")
while True:
    num = int(input("Diga um valor: "))
    resp = ' '
    comp = randint(1, 10)
    total = num + comp
    while resp not in 'PI':
        resp = str(input("Par ou Ímpar? [P/I] ")).upper().strip()[0]
    print(f"Você jogou {num} e o computador {comp}. O total deu {total}")
    if resp == 'P':
        if total %2 == 0:
            print("Voce ganhou!")
            soma+=1
        else:
            print("VOCE PERDEU")
            break
    elif resp == 'I':
        if total % 2 ==1:
            print("Voce ganhou!")
            soma+=1
        else:
            print("Voce perdeu")
            break
    print("Vamos jogar novamente")
    sleep(1)
print(f"GAMER OVER, VOCE VENCEU {soma} vezes.")