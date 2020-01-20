# PARTICIONANDO UM NÚMERO DE 0 A 9999 E EXIBINDO SUAS CASAS

n = int(input('Digite um número de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('A unidade do número {} é: {}'.format(n, u))
print('A dezena do número {} é: {}'.format(n, d))
print('A centena do número {} é: {}'.format(n, c))
print('O milhar do número {} é: {}'.format(n, m))
