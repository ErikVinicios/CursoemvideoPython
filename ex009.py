num = int(input('Digite um número: '))
cont = 1
while cont <= 10:
    print(f'\033[34m{num}\033[m X \033[34m{cont}\033[m = \033[36m{num*cont}')
    cont+=1