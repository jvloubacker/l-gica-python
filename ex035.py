print('-=-' * 15)
print('Analisador de triângulos')
print('-=-' * 15)
r1 = float(input('\033[1;35mPrimeiro segmento:\033[m '))
r2 = float(input('\033[1;33mSegundo segmento:\033[m '))
r3 = float(input('\033[1;34mTerceiro segmento:\033[m '))
if (r1 < r2 + r3) and (r2 < r1 + r3) and r3<r1 + r2:
    print('\033[1;31;40mOs segementos acima PODEM FORMAR um triângulo\033[m')
else:
    print('\033[35;40mOs segmentos acima NÃO PODEM FORMAR um triângulo\033[m')