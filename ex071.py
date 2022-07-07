sacar = int(input('QUal o valor à ser sacado? '))
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
while True:
    while sacar != 0:
        if sacar % 50 == 0:
            sacar -= 50
            nota50 += 1
        elif sacar % 20 == 0:
            sacar -= 20
            nota20 += 1
        elif sacar % 10 == 0:
            sacar -= 10
            nota10 += 1
        elif sacar % 1 == 0:
            sacar -= 1
            nota1 += 1
    if sacar == 0:
        break
print('\n\033[1:37m---------- CÉDULAS RECEBIDAS ----------\033[m')
if nota50 > 0:
    print(f'\033[1:33m{nota50}\033[m notas de \033[1:32mR$50.00\033[m')
if nota20 > 0:
    print(f'\033[1:34m{nota20}\033[m notas de \033[1:32mR$20.00\033[m')
if nota10 > 0:
    print(f'\033[1:31m{nota10}\033[m notas de \033[1:32mR$10.00\033[m')
if nota1 > 0:
    print(f'\033[1:37m{nota1}\033[m notas de \033[1:32mR$1.00\033[m')