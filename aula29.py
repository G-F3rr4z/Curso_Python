"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input ('Vou dobrar o valor que você colocar: ')

try:
    print('STR', numero_str)
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'O dobro do {numero_str} é {numero_float * 2 }')
except:
    print('Isso nãoé um numero')




# print(numero_str.isdigit ())

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro do {numero_str} é {numero_float * 2 }')
# else:
#     print('Isso nãoé um numero')




















