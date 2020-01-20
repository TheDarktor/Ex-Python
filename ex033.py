# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

s = int(input('Digite o salário do funcionário: '))

if s > 1250:
    a = int(s * 0.10)
    sn = float(s + a)
else:
    a = int(s * 0.15)
    sn = float(s + a)

print('O salário com aumento corresponde a {} reais'.format(sn))
