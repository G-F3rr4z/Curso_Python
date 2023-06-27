palavra_secreta = 'paralelepipedo'
lista = ['_'] * len(palavra_secreta)
numero_max_tentativas = len(palavra_secreta) * 2
tentativa_atual = 0

print('Adivinhe a palavra:', ' '.join(lista))

while tentativa_atual <= numero_max_tentativas:
    entrada = input('Digite uma letra: ')

    if entrada in lista:
        print('Você já acertou essa letra.')
    else:
        tentativa_atual += 1

    acertos = 0
    for i, letra in enumerate(palavra_secreta):
        if letra == entrada:
            lista[i] = entrada
            acertos += 1

    if acertos > 0:
        print('A palavra:', ' '.join(lista))
    else:
        print('Essa letra não está na palavra.')

    if '_' not in lista:
        print('Você acertou a palavra!')
        break

print('A palavra secreta era:', palavra_secreta)


