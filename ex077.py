palavras = ('aprender', 'programar', 'linguagem', 'python', 
            'curso', 'gratis', 'estudar', 'praticar', 
            'trabalhar', 'mercado', 'programador', 'futuro') 
for pav in palavras:
    print(f'\nNessa palavra \033[01;31m{pav}\033[m temos', end=' ')
    for letras in pav:
        if letras in 'aeiou':
            print(f'{letras}',end=' ')