from random import randint
from time import sleep
números = []


def sorteio(qnt):
    print(f'Sorteando \033[1:32m{qnt} VALORES\033[m da lista:',end=' ' )
    for c in range(qnt):
        números.append(randint(1,10))
    for c in números:
        sleep(1)
        print(f'\033[1:32m{c}\033[m',end=' ')
    print()


def somaPAR(lista):
    s = 0
    print(f'\033[1:34mSOMANDO\033[m todos os \033[1:34mVALORES PARES\033[m de \033[1:34m{lista}\033[m, temos ',end='')
    for c in lista:
        if c % 2 == 0:
            s += c
    print(f'\033[1:34m{s}\033[m')


sorteio(5)
somaPAR(números)