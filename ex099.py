from time import sleep


def maior(*num):
    sleep(1)
    m = 0
    print('\033[1:31mAnalisando os valores informados...\033[m')
    for p,c in enumerate(num):
        print(f'\033[1:32m{c}\033[m',end=' ')
        if p == 1 or m < c:
            m = c
    print(f'foram informados \033[1:32m{len(num)} VALORES\033[m ao todo')
    print(f'O \033[1:33mMAIOR VALOR\033[m informado foi \033[1:33m{m}\033[m')
    print('\033[1:39m-=\033[m' * 30)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
