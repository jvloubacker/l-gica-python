def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade <= 16:
        return f'Com idade {idade}: NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com idade {idade}: VOTO OPCIONAL'
    else:
        return f'Com idade {idade}: VOTO OBRIGATORIO'


num = int(input('Ano de nascimento: '))
print(voto(num))
