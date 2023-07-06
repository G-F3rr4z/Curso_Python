x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


# def soma(x, y):
#     return x + y
# soma(200,300)


def soma(*args):
    # print(args, type(args))
    total = 0
    for numero in args:
        print('Total: ', total, '+', numero)
        total = total + numero
        print('Total: ', total)


soma(1,2,3,4,5,6)


