# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# s1 = set('Luiz')
# # s1 = set()  # vazio
s1 = set({1, 2, 3, 1, 4, 5, 1 })  # com dados
print(s1)
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
# s1 = { 1, 2, 3}
# s1 = set()
# s1.add(1)
# s1.add('Gabriel')
# s1.update(('Ola mundo', 1,2,3,4,5,6))
# s1.discard(6)

# print(s1)

# Métodos úteis: 
# add, update, clear, discard

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
# s1 = {1,2,3}
# s2 = {2,4,3}
# s3 = s1 | s2
# s3 = s1 & s2
# s3 = s2 - s1
# s3 = s2 ^ s1
# print(s3)

