from random import randint
from time import sleep
eu = pc = alt = altPC = c = 0
while True:
    while eu != 1 and eu != 2:
        eu = int(input('''\nEu escolho:
[1] PAR
[2] IMPAR
Resposta: '''))
        if eu != 1 and eu != 2:
            print('\n\033[1:32mALTERNATIVA INVÁLIDA.\033[m ')
    if eu == 1:
        eu = 'PAR'
        pc = 'IMPAR'
    elif eu == 2:
        eu = 'IMPAR'
        pc = 'PAR'
    alt = int(input('Digite um número de 1 à 10: '))
    altPC = randint(0,10)
    print('\n\033[1:38mPROCESSANDO...\033[m')
    sleep(3)
    print(f'''\n\033[1:32mEU: {alt}\033[m
\033[1:31mCOMPUTADOR: {altPC}\033[m
\n\033[1:39mRESULTADO: {alt + altPC}\033[m''')
    if (alt + altPC) % 2 == 0 and eu == 'PAR':
        print('\n\033[1:32mEU VENCI\033[m! ')
        c += 1
    else:
        break
print(f'\n\033[1:31mGAME OVER!\033[1:32m Você ganhou {c} vezes.\033[m')


