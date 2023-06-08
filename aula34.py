
# """
# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
# """


entrada = input('Qual seu primeiro nome? ')


if len(entrada) < 1:
    print("Digite uma letra")
if len(entrada) >= 1 and len(entrada) <= 4:
    print('Seu nome é curto')
elif len(entrada) >= 5 and len(entrada) <= 6:
    print('Seu nome é normal')
elif len(entrada) > 6:
    print('Seu nome é muito grande')