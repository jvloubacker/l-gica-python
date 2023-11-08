from time import sleep
import emoji
print('-=' *34)
print('CONTAGEM REGRESSIVA PARA O LANÇAMENTO DOS FOGUETES DA SPACE-X!!!')
print('-=' *34)
for cont in range(10,-1,-1):
    print(cont)
    sleep(1)
print(emoji.emojize(':foguete:'*10, language='pt'))
print('FOGUETES LANÇADOS COM SUCESSO.')