# Manipulando chaves e valores em dicionarios

#CRUDS

pessoa = {}

chave = 'nome' #Cria uma chave para o nome
pessoa[chave] = 'Gabriel Ferraz' # Aqui voce anexou a chave dentro de uma Chave Dinamica
pessoa['sobrenome'] = 'Rezende' # aqui foi criado mais uma chave para o sobrenome

print(pessoa[chave])

pessoa[chave] = 'maria' #aqui estamos criando uma chave com o mesmo nome do inicio porem o item dentro da chave ser[a outro, para mostrar que podem ser alteraos ao longo do codigo]

del pessoa['sobrenome'] # aqui nos deletamos a chave sobrenome que foi criado apenas para veriricar

print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None: # aqui a gente verificou se a chave 'sobrenome' existe, se senao existir ele envia 'nao existe'. apenas para nao travar o programa com erro.
    print('nao existe')
else:
    print(pessoa['sobrenome']) 