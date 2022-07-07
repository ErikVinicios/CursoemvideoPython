qnt = int(input('Quantidade de elementos: '))
n = 1
f = 0
c = 0
while c < qnt:
    print(f'\033[1:33m{f}\033[m - \033[1:36m{n}\033[m', end = ' - ')
    f += n
    n += f
    c += 2
