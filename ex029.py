# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n = int(input('Digite um número qualquer: '))
r = int(n % 2)

if r == 1:
    print('O número {} é ímpar'.format(n))
else:
    print('O número {} é par'.format(n))
