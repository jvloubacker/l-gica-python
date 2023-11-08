nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
média = (nota1 + nota2) / 2

print(f"Com a nota {nota1} e {nota2}, você ficou com {média} de média.")

if média >= 5 and média < 7:
    print(f'O aluno com a {média} de média, está de RECUPERAÇÃO.')

elif média < 5:
    print(f'Com essa média, você está REPROVADO!')

else:
    print(f'Você foi APROVADO, parabéns!')