n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
alt = 0
while alt != 5:
    print('')
    alt = int(input('''O QUE DESEJA FAZER?
(1) \033[1:33mSOmAR\033[m
(2) \033[1:34mMULTIPLICAR\033[m
(3) \033[1:35mMAIOR\033[m
(4) \033[1:36mNOVOS NÚMEROS\033[m
(5) \033[1:31mFECHAR PROGRAMA\033[m
SUA OPÇÃO: '''))
    if alt == 1:
        print('')
        print(f'\033[1:33m{n1} + {n2} = {n1 + n2}\033[m')
    elif alt == 2:
        print('\n')
        print(f'\033[1:34m{n1} X {n2} = {n1 * n2}\033[m')
    elif alt == 3:
        if n1 > n2:
            print('')
            print(f'\033[1:35mO 1º número ( {n1} ) é maior.\033[m ')
        else:
            print('')
            print(f'\033[1:35mO 2º número ( {n2} ) é maior. \033[m')
    elif alt == 4:
        print('')
        n1 = int(input('1º número: '))
        n2 = int(input('2º número: '))
    elif alt == 5:
        print('')
        print('\033[1:32mPROGRAMA FINALIZADO.\033[m ')
    else:
        print('')
        print('\033[1:31malternativa inválida.\033[m')