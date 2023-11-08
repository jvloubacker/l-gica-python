from math import radians, sin, cos, tan
angulo= float(input('Digite um ãngulo: '))
radiano = radians(angulo)
sin = sin(radiano)
cos = cos(radiano)
tan = tan(radiano)
print(f'O valor do seno é: {sin:.2f}')
print(f'O valor do cosseno é: {cos:.2f}')
print(f'O valor do tangente é: {tan:.2f}')