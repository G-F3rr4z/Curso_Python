# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um numero é par ou impar.
# Retorne se o numero é par ou impar.
x, y, *resto = 1,2,3,4,5

def multiplicacao(*args): #função que multiplica argumentos.
    total = 1 # iniciando em 1 porque qualquer multiplicador por 0 da 0.
    for numero in args:
        total *= numero
    return total

multiplicador = multiplicacao(x,y,*resto) # total esta na variavel Multiplicador
print(multiplicador) # mostrando o valor da variavel.

def par_impar():
    verificador = 2
    resto_divisao = multiplicador % verificador # verifica se o resto da divisão(%) é igual a 0, para definir se é par ou impar.
    
    if resto_divisao == 0: # se o valor verificado for igual a 0, entao o numero é par.
        print('esse numero é par')
    else:
        print('esse numero é impar')

par_impar()



