media = {'Nome':'', 'media': '', 'Situação': ''}
nota = list()
media['Nome'] = str(input('Nome do aluno: '))
media['media'] = float(input('Media do aluno: '))
if media['media'] >= 7:
    media['Situação'] = 'Aprovado'
elif 5 < media['media'] < 7:
    media['Situação'] = 'Recuperação'
else:
    media['Situação'] = 'Reprovado'
nota.append(media.copy())
for k,v in media.items():
    print(f'{k} é igual a {v}.')