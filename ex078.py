lista = []
maior = 0
menor = 0
for c in range(5):
    lista.append(int(input(f'DIgite o {c}º valor: ')))
print(f'Os números digitados foram ',end = '')
for c in lista:
    print(f'\033[1:32m{c}\033[m',end=' ')
print(f'\nO \033[1:34mMAIOR número\033[m foi o \033[1:34m{max(lista)}\033[m, que está na \033[1:34mPosição ',end='')
for p,n in enumerate(lista):
    if n == max(lista):
        print(p, end = ' ')
print(f'\033[m\nO \033[1:33mMENOR número\033[m foi o \033[1:33m{min(lista)}\033[m, que está na \033[1:33mPosição ',end='')
for p,n in enumerate(lista):
    if n == min(lista):
        print(p, end = ' ')