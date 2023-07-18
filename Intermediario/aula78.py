pessoa = {

'nome': 'Gabriel',
'sobrenome' : 'Ferraz',
'idade' : 28,

}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
# print(len(pessoa))
# print(tuple(pessoa.keys()))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))


# for chave, valor in pessoa.items():
#     print(chave, valor)

# for valor in pessoa.values():
#     print(valor)


# for chave in pessoa: 
#     print(chave)
