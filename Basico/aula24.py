# nome = 'Gabriel'


# # print(nome[2])

# print(nome[-4])




# print('a' in nome )

# print ('z' in nome)
# print ('el' not in nome)

nome = input ('Digite seu nome: ')

encontrar = input ('Digite o que você deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}.')
else:
    print(f'{encontrar} nao está em nome.')
