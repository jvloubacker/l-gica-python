sexo = str(input('Digite seu sexo: [M/F] ')).upper()[0].strip()
while sexo not in 'FM':
        sexo = str(input('Dados invalidos, tente novamente [M/F]: ')).upper()[0]
print(f"Sexo {sexo} registrado com sucesso.")
