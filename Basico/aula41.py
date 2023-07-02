""" CALCULADORA PYTHON COM WHILE """ 



while True:

    # parte de entrada de dados da calculadora
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+ - / *): ')
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    # conversão de valores de INTEIRO para FLOAT
    try:
        num_1_float = float (numero_1)
        num_2_float = float (numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um dos numeros não sao validos')
        continue

    # verificação dos operadores
    operadores_validos = '+-/*'

    if operador not in operadores_validos:
        print('operador invalido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    # ponto de validação de cálculos
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =', num_1_float * num_2_float)
    else:
        print('Nao deveria dar esse erro.')

    # parte de saída da calculadora
    sair = input ('Quer sair da caluladora? ').lower().startswith('s')

    if sair is True:
        break



