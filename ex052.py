n = int(input('Número: '))
m = 0
for c in range(1,n+1):
    if n % c == 0:
        print('\033[1:32m',end='')
        m += 1
    else:
        print('\033[1:31m', end='')
    print(f'{c}',end=' ' )
if m == 2:
    print('\n\033[1:32mPRIMO!\033[m ')
else:
    print('\n\033[1:31mNão é primo. \033[m')