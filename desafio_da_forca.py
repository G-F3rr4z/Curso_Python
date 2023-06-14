# lista = []
# print(lista)

# lista.append('ola')
# print(lista)

# lista.append(8)
# print(lista)

# lista.pop(1)
# print(lista)

# lista.insert(5, 3)
# print(lista)




palavra_secreta = 'paralelepipedo'
lista = ['_']*len(palavra_secreta)
numero_max_tentativas = len(palavra_secreta)*2
tentativa_atual = 0

print('Adivinhe a palavra ', lista)

while tentativa_atual <= numero_max_tentativas:

    entrada = input('Digite uma letra: ').lower()

    if entrada in lista:
        print('Ja acertou essa letra.')    
    else:
        tentativa_atual += 1

    if entrada in palavra_secreta:
        print(entrada)
        posicao = (palavra_secreta.index(entrada))
        lista [posicao] = entrada
        print(lista)

    else:
        print('Essa letra não está na palavra')

    if '_' not in lista:
        print('Você acertou :D ')
        break



print(palavra_secreta)





