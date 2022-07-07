n = int(input('Digite um número: '))

if n % 2 == 0:
    print('Este número é \033[4:36mPAR\033[m. ')
else:
    print('Este número é \033[4:36mIMPAR\033[m. ')
