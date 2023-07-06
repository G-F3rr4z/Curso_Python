x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def soma(*args):
    total = 0
    for numero in args:
        total = total + numero    
    return total

soma_1_2_3_4_5_6_7_8_9_10 = soma(1,2,3,4,5,6,7,8,9,10)
print(soma_1_2_3_4_5_6_7_8_9_10)

print_1_2_3_4_5_6_7_8_9_10 = (1,2,3,4,5,6,7,8,9,10)
print(print_1_2_3_4_5_6_7_8_9_10)

numeros = 1,2,3,4,5,6,7,8,9,10
outra_soma = soma(*numeros)
print(outra_soma)

numeros = 1,2,3,4,5,6,7,8,9,10
print(sum(numeros))





