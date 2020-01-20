# ALGORITIMO FEITO PARA CALCULAR A QUANTIDADE NBCESSÁRIA DE TINTA PARA PINTAR UMA PAREDE, LEVANDO EM CONSIDERAÃO QUE
# 1 LITRO DE TINTA É O SUFICIENTE PARA 2M²
al = float(input('Digite a altura da parede: '))
la = float(input('Digite a largura da parede: '))
a = float(al*la)
q = float(a/2)
print('Tamanho da área em m²: {}'.format(a))
print('Litros de tinta necessários: {}'.format(q))
