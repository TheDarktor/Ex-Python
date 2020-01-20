# ALUGUEL DE CARRO CONSIDERANDO QUE 1 DIA CUSTE R$60 E CADA KM PERCORRIDO CUSTE R$0,15
d = int(input('Digite o número de dias que o carro foi utilizado: '))
k = int(input('Digite o número de quilômetros percorridos: '))
pd = float(d*60)
pk = float(k*0.15)
pf = float(pd+pk)
print('O valor total a ser pago é de: {:.2f}'.format(pf))
