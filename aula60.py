"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

    10 9  8  7  6  5  4  3  2
    1  2  4  8  2  9  2  9  6
    220 * 10 = 2200
    2200 % 11 = 0


Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

# cpf = input('Insira o seu CPF (digite apenas numeros.): ')

cpf_enviado_cliente = input('Digite o seu CPF, digite somente numeros:  ')
nove_digitos = cpf_enviado_cliente[:9]
dez_digitos = cpf_enviado_cliente[:10]
contador_regressivo_1 = 10
resultado_1 = 0
multiplicacao_1 = 0
resultado_2 = 0
multiplicacao_2 = 0
contador_regressivo_2 = 11

for digito_1 in nove_digitos:
    resultado_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
    multiplicacao_1 = resultado_1 * 10
    digito_1 = multiplicacao_1 % 11

for digito_2 in dez_digitos:
    resultado_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
    multiplicacao_2 = resultado_2 * 10
    digito_2 = multiplicacao_2 % 11

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_cliente == cpf_gerado:
    print('CPF: ' f'{cpf_enviado_cliente} é Válido')
else:
    print('CPF: ' f'{cpf_enviado_cliente} é Inválido')



