# exemplo de uso de set 
letras = set()

while True:
    letra = input('Digite uma letra: ')
    letras.add(letra)

    if 'l' in letras:
        print('Parabens voce encontrou a seta secreta')
        break
    print(letras)

