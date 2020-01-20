# ALGORITIMO QUE RECEBE O NOME DE UMA PESSOA E RETORNA AS SEGUINTES INFORMAÇÕES:
# Nome com todas as letras maiúsculas e minúsculas.
# Quantas letras tem o nome completo (sem considerar os espaços)
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome) - nome.count(' ')))

nome_split = nome.split()
print('Seu primeiro nome possui {} letras'.format(len(nome_split[0])))
