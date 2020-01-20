# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Insira a velocidade do carro: '))
if v > 80:
    vu = int(v-80)
    m = int(vu * 7)
    print('Você foi multado, o valor a ser pago é de {} reais'.format(m))
else:
    print('Você não foi multado')
