# IDENTIFICANDO O TIPO PRIMITIVO E EXIBINDO O MAXIMO DE INFORMAÇÕES DE UMA VARIÁVEL

var1 = input('Digite algo: ')

print(type(var1))
print('alpha: {}'.format(var1.isalpha()))
print('alphanum: {}'.format(var1.isalnum()))
print('ascii: {}'.format(var1.isascii()))
print('decimal: {}'.format(var1.isdecimal()))
print('digit: {}'.format(var1.isdigit()))
print('identifier: {}'.format(var1.isidentifier()))
print('lower: {}'.format(var1.islower()))
print('numeric: {}'.format(var1.isnumeric()))
print('printable: {}'.format(var1.isprintable()))
print('space: {}'.format(var1.isspace()))
print('title: {}'.format(var1.istitle()))
print('upper: {}'.format(var1.isupper()))
