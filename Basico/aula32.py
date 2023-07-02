"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input('Digite um número: ')

# if numero.isdigit():
#     numero_int = int(numero)
#     par_impar = numero_int % 2 == 0
#     par_impar_texto = 'impar'


#     if par_impar:
#         par_impar_texto = 'par'



#     print(f'o numero {numero_int} é {par_impar_texto}')
# else:
#     print('Voce nao digitou um numero inteiro')


numero = input('Digite um número: ')

try:
    numero_int = float(numero)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'
    print(f'o numero {numero_int} é {par_impar_texto}')

except:
    print('Voce nao digitou um numero inteiro')
