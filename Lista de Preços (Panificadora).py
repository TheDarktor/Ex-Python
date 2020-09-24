print('-'*58)
x = float(input('Insira o valor desejado para criar a tabela de preços: '))
y = x
z = 1
print('-'*58)
print('')
print('Preço do Pão: R$ {}'.format(x))
print('Panificadora Pão de Ontem - Tabela de preços')
print('')

while z <= 50:
    print('{} - R$ {:.2f}'.format(z,x))
    x += y
    z += 1
print('-'*60)