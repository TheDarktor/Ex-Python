# EXIBINDO EM TRUE OU FALSE SE O NOME INSERIDO POSSUI "SILVA"

nome = str(input('Digite um nome completo: ')).strip()

print('O nome possui silva? {}'.format('silva' in nome.lower()))
