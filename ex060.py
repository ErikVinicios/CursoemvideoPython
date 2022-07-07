from math import factorial
num = int(input('DIGITE UM NÚMERO: '))
c = num
print('')
print(f'\033[1:31m{num}! \033[m= ', end = '')
while c > 0:
    print(f'\033[1:36m{c}', end = '' )
    print(' X ' if c > 1 else '\033[m = ', end = '')
    c -= 1
print(f'\033[1:31m{factorial(num)}\033[m')
print('')
print('\033[1:32mPROGRAMA FINALIZADO.\033[m')