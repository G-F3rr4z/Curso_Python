'''
split e join com list e str
split - divide uma string
join - une uma string

'''
frase = 'Olha o que eu tenho comigo, uau'
lista_frases_crua = frase.split(',')
lista_frases = []


for indice, frase in enumerate(lista_frases_crua):
    lista_frases.append(lista_frases_crua[indice].strip())

print(lista_frases_crua)
print(lista_frases)

frases_unidas = ', '.join(lista_frases)
print(frases_unidas)

