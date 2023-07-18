p1 = {
    'nome': 'Gabriel',
    'sobrenome' : 'Ferraz',
    'idade' : 28
}

# print(p1['nome'])
# print(p1.get('nome', 'nao existe mais sobrenome'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#         'idade' : 28
# 
#})

# p1.update(nome = 'Taina', idade = 27)

tupla = (('nome', 'novo valor'), ('idade', 33))
lista = [['nome', 'novo valor'], ['idade', 33]]
p1.update(lista)
p1.update(tupla)
print(p1)
