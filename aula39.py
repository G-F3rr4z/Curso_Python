# """
# Iterando strings com while
# """
# # #     0123456789101112
# nome = 'Gabriel Ferraz'  # Iteráveis
# # #     13121110987654321

# Faça uma nova stringo retornar '*G*a*b*r*i*e*l* *F*e*r*r*a*z'

nome = 'Gabriel Ferraz'
indice = 0
novo_nome = ''
while indice < len(nome):
    
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)



#print( '*'.join(list('Gabriel Ferraz'))) -- comentario de @luabida



