s = 0
m = 0
c = 0
alt =\
maior = 0
menor = 0
while alt != 'N':
    num = int(input('Digite um número: '))
    s += num
    c += 1
    if c == 1:
        maior = menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    alt = input('Deseja inserir mais números? [S/N]').upper().strip()
m = s / c
print('')
print(f'''\033[1:39mDos {c} números digitados:\033[m
\033[1:36m{maior} Foi o MAIOR\033[m
\033[1:31m{menor} Foi o MENOR\033[m
\033[1:33m{m:.1f} Foi a MÉDIA\033[m''')