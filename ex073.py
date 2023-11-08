times = 'Botafogo','Palmeiras','Grêmio','Bragantino','Fluminense','Athletico-PR','Flamengo','Fortaleza','Atlético-MG',\
    'Corinthians','Cuiabá','Cruzeiro','Internacional','São Paulo','Vasco','Goiás','Bahia','Santos','América-MG',\
    'Coritiba'
for pos, t in enumerate (times):
    print(f"Classificação, serie A: {pos +1}ª {t} ")
print("-=" *21)
print(f"Os 5 primeiros colocados são: {times[0:5]}")
print("-=" *14)
print(f"Os últimos 4 colocados são: {times[16:]}")
print("-=" * 14)
print(sorted(times))
print("-=" *15)
print(f"O flamengo está na {times.index('Flamengo')+1}ª posição.")