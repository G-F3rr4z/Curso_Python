"""
Exercicio
Exiba os índices da lista
"""

lista = ['Maria', 'Helena', 'Luiz']
# indice = 0
lista.append('Ferraz')

indices = range(len(lista))

print(indices)
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
    # indice += 1



