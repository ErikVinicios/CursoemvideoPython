num = int(input('Digite um número de 0 a 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'Unidade: \033[32m{u}\033[m\nDezena: \033[31m{d}\033[m\nCentena: \033[35m{c}\033[m\nMilhar: \033[33m{m}\033[m')