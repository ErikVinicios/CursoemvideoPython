matriz = [[], [], []]
somaP = soma3 = maior2 = 0
for i in range (3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite um número para a posição [{i},{j}]: ')))
print('-='*40)
for i in range(3):
    for j in range(3):
        print(f'[\033[1:34m{matriz[i][j]:^5}\033[m]',end=' ')
        if i == 0:
            maior2 = matriz[1][0]
        elif maior2 < matriz[1][j]:
            maior2 = matriz[1][j]
    print('')
for bloco in matriz:
    soma3 += bloco[2]
    for n in bloco:
        if n % 2 == 0:
            somaP += n
print('-='*40)
print(f'\033[1:32mA \033[1:33mSOMA\033[1:32m dos valores \033[1:33mPARES\033[m \033[1:32mé \033[1:33m{somaP}\033[m')
print(f'\033[1:32mA \033[1:31mSOMA\033[1:32m dos valores da \033[1:31mTERCEIRA COLUNA \033[1:32mé \033[1:31m{soma3}\033[m')
print(f'\033[1:32mO \033[1:34mMAIOR VALOR \033[1:32mda\033[1:34m LINHA 2 \033[1:32mé \033[1:36m{maior2}\033[m')