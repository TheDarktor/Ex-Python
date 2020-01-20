# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

d = int(input('Digite a Distância da viagem: '))

if d <= 200:
    v = float(d * 0.50)
else:
    v = float(d * 0.45)

print('O valor da viagem é de {} reais'.format(v))
