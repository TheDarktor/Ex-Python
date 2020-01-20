# MOSTRANDO O DOBRO, TRIPLO E RAIZ QUADRADA DE UM NÚMERO
n = int(input('Digite um número: '))
d = int(n*2)
t = int(n*3)
r = float(n**0.5)
print('O número é: {}, seu dobro é: {}, seu triplo é: {}, e sua raiz quadrada é: {:.3f}'.format(n, d, t, r))
# {:.3f} diz que só é necessário apresentar 3 casas decimais
