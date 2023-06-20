"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
# """


# nome = 'Gabriel'
# noutra_variavel = nome
# nome = 'Ferraz'

# print(nome)
# print(noutra_variavel)

lista_a = ['Gabriel', 'Ferraz']
lista_b = lista_a.copy()
lista_a[0] = 'Qualquer coisa'

print(lista_b)
print(lista_a)



