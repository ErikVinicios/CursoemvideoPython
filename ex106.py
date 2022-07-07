from time import sleep


def Pyhelp(comando):
    c = f'Acessando o manual do comando {comando}'
    esp = len(c) + 2
    print('\033[39:44m-' * esp)
    print(f' {c} ')
    print('-' * esp)
    sleep(1)
    print(f'\033[7:39:40m')
    return help(comando)


while True:
    print('\033[39:43m-' * 27)
    print('  SISTEMA DE AJUDA PYHELP ')
    print('-' * 27)
    f = str(input('\033[mFunção ou biblioteca > ').strip().lower())
    if f == 'fim':
        print('\033[41m-' * 12)
        print('  ATÉ LOGO ')
        print('-' * 12)
        break
    Pyhelp(f)
    print('\033[m')
