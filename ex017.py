# CALCULANDO A HIPOTENUSA COM BASE NO CATETO OPOSTO E ADJACENTE
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = hypot(co, ca)
print('O valor da hipotenusa é: {:.2f}'.format(hi))
