num = int(input('1º número da PA: '))
r = int(input('Razão: '))
print('')
qnt = 10
PA = num
c = 0
while c < qnt:
    print(f'\033[1:36m{PA}\033[m', end = '\033[1:35m → \033[m')
    PA += r
    c += 1
print('\n')
print('\033[1:32mPROGRAMA FINALIZADO.\033[m')
