a = int(0)
b = int(1)
c = int(15)
cont = int(0)
print('-'*54)
print('Os 15 primeiros termos na escala de fibonacci são:')
print('{}, {}'.format(a, b), end="")
while cont <= 12:
    d = a + b
    print(', {}'.format(d), end="")
    a = b
    b = d
    cont += 1