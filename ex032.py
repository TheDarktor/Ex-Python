# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 < n2 and n1 < n3:
    menor = int(n1)

if n2 < n1 and n2 < n3:
    menor = int(n2)

if n3 < n1 and n3 < n2:
    menor = int(n3)

# --------------------------------------------

if n1 > n2 and n1 > n3:
    maior = int(n1)

if n2 > n1 and n2 > n3:
    maior = int(n2)

if n3 > n1 and n3 > n2:
    maior = int(n3)

print('O menor número é {} e o maior é {}'.format(menor, maior))
