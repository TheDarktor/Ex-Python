# EXIBINDO O PREÇO DE UM PRODUTO PORÉM COM 5% DE DESCONTO
p = float(input('Digite o preço do produto: '))
d = float(p*0.05)
pf = float(p-d)
print('O mesmo produto com 5% de desconto vale: {}'.format(pf))