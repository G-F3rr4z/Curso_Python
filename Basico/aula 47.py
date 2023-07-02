"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""



palavra = 'Dunossauro'
quantidade_maxima_de_tentativas = len(palavra)*2
tentativas_usadas = 0

while tentativas_usadas <= quantidade_maxima_de_tentativas:

    entrada = input ('Digite uma letra: ')


    if entrada in palavra:
        print(entrada)
    else:
        print('Não existe essa letra')
    
    tentativas_usadas = tentativas_usadas + 1
    print(f'tentativa:', tentativas_usadas)



if entrada == True:
    print(entrada)



# for letra in palavra:
#     print(letra)