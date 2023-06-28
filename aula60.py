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