"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Gabriel', 'Ferraz', 'Rezende']
lista.append('Andrade')


# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

for indice, nome in enumerate(lista):
    print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')

# for indice, nome in enumerate(lista):
#     print(indice, nome, lista[indice])