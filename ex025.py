# EXIBINDO QUANTAS VEZES A LETRA A APARECE, E QUAL SUA PRIMEIRA E ULTIMA OCORRÊNCIA

f = str(input('Digite uma frase qualquer: ')).strip()

print('A letra A apareceu {} vezes'.format(f.lower().count('a')))
print('A primeira letra A apareceu na posição {}'.format(f.lower().find('a')+1))
print('A ultima letra A apareceu na posição {}'.format(f.lower().rfind('a')+1))
