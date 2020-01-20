# EXIBINDO SOMENTE O PRIMEIRO E ULTIMO NOME DE UMA PESSOA

n = str(input('Digite o nome completo: ')).strip()
nome = n.split()

print('Prazer {} {}'.format(nome[0], nome[len(nome) - 1]))
