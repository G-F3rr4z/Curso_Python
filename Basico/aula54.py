"""
faça uma lista de compras com listas
o usuario deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Nao permita que o porgrama quebre com erros de indices inexistentes na lista.
"""
lista = []
import os

while True:
    entrada = input ('Inseria uma opção\n[i]nserir, [a]pagar, [l]istar: ').lower()

    if entrada == 'i':
            os.system('cls')
            inserir = input('Qual item deseja inserir? ')
            lista.append(inserir)

    elif entrada == 'a':
            for apagar in entrada:
                apagar = input('Qual indice deseja apagar? ')

            try:
                apagar_int = int(apagar)
                del lista[apagar_int]
            except ValueError:
                  print('Insira um valor Int.')
            except IndexError:
                  print('Indice não existe na lista')
            except Exception:
                  print('Erro desconhecido')

    elif entrada == 'l':
                os.system('cls')
                for i, valor in enumerate(lista):
                    print(i, valor)
    else:
        print('Não existe essa opção.')
        