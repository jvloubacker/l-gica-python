print('-=-' * 9)
print('      GERADOR DE PA     ')
print('-=-' * 9)
primeiro = int(input("DIGITE O PRIMEIRO TERMO: "))
razao = int(input("DIGITE A RAZÃO: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, end=' → ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input("\nQuantos termos você quer mostrar a mais? "))
print(f"Progressão finalizada com sucesso, foi mostrado {total} termos.")
