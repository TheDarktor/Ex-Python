# CALCULANDO O SENO, COSSENO E TANGENTE DE UM NÚMERO

from math import radians, sin, cos, tan

an = float(input('Digite o ângulo: '))
sen = float(sin(radians(an)))
cos = float(cos(radians(an)))
tan = float(tan(radians(an)))

print('O SENO de {} é: {:.2f}'.format(an, sen))
print('O COSSENO de {} é: {:.2f}'.format(an, cos))
print('A TANGENTE de {} é: {:.2f}'.format(an, tan))
