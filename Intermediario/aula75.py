# Exercicios
# Crie funcoes que duplicam, triplicam e quadriplicam o numero recebido como parametro
def criar_multiplicador (multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))



# Exercicios
# Crie funcoes que duplicam, triplicam e quadriplicam o numero recebido como parametro


# def entrada(expressao):
#     return expressao

# duplicar = entrada( int(2))
# triplicar = entrada( int(3))
# quadriplicar = entrada( int(4))

# for numero in [int('10')]:
#     print(duplicar*(numero))
#     print(triplicar*(numero))
#     print(quadriplicar*(numero))

