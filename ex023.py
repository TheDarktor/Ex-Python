# EXIBINDO EM TRUE OU FALSE SE A CIDADE INSERIDA COMEÇA COM A PALAVRA "SANTO"

cidade = str(input('Digite o nome de uma cidade: ')).strip()

print(cidade[:5].lower() == 'santo')
