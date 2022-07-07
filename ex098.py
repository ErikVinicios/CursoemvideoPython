from time import sleep


def contador(i, m, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'\033[1:32mContagem de {i} até {m} de {p} em {p}:\033[m ')
    sleep(1)
    if i > m:
        p *= -1
    for c in range(i, m, p):
        sleep(0.5)
        print(f'\033[1:33m{c}\033[m', end=' ')
    sleep(0.5)
    print(f'\033[1:33m{m}\033[m')
    print('\033[1:37m-=\033[m' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
print('\033[1:36mAgora é a sua vez:\033[m')
inicio = int(input('\033[1:36mInicio:\033[m '))
meio = int(input('\033[1:36mMeio:\033[m '))
passo = int(input('\033[1:36mPasso:\033[m '))
contador(inicio, meio, passo)
