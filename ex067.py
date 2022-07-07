while True:
    c = 1
    n = int(input('\nDigite um número POSITIVO para ver sua tabuada: '))
    print('')
    if n < 0:
        print('\033[1:32mPROGRAMA FINALIZADO! VOLTE SEMPRE.\033[m ')
        break
    else:
        for c in range(1,11):
            print(f'\033[1:33m{n} \033[1:35mX \033[1:34m{c} \033[1:31m= \033[1:39m{n * c}\033[m')

