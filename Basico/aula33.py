"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada = input('Agora são quantas horas? ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print(f'Bom dia, agora são exatamente {hora} horas')
    elif hora >= 12 and hora <= 17:
        print(f'Boa tarde, agora são exatamente {hora} horas')
    elif hora >= 18 and hora <= 23:
        print(f'Boa noite, agora são exatamente {hora} horas')
    else:
        print('Esse hora não existe!')
except:
    print('Por favor digite número inteiro')
