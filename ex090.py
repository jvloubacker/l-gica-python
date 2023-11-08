media = {'Nome':'', 'Media':'','Situação':''}
nota = list()
media['Nome']= str(input("Digite o seu nome: "))
media['Media']= float(input(f'Média de {media["Nome"]}: '))
nota.append(media.copy())
if media['Media'] < 6.0:
    media['Situação'] = 'Reprovado'
else:
    media['Situação']= 'Aprovado'
for k,v in media.items():
    print(f'{k} é igual a {v}')

