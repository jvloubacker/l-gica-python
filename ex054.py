from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu: '))
    idade = atual - nasc
    if idade >= 18:
        totmaior+= 1
    else:
        totmenor += 1
print(f'{totmenor} sao menores de idade Menor idade!')
print(f'{totmaior} pessoas são maiores de idade.')
