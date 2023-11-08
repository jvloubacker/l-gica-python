largura = float(input('Qual é a largura da parede? '))
altura = float(input('Qual é a altuta da parede? '))

tam = largura * altura

print(f"A sua parede é de {tam:.2f}m²")

tinta = tam / 2
print(f'Você vai usar {tinta:.3f} litros de tinta ! ')