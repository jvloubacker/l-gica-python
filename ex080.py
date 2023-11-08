valores = []
for c in range(0, 5):
    n = int(input("Digite um número: "))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print("ADICIONADO AO FINAL DA LISTA")
    else:
        pos = 0
        while pos< len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'ADICIONADO NA POSIÇÃO {pos} da lista')
                break
            pos += 1
print(f'Os valores corretos {valores}')
