matriz = [[],[],[]]
for i in range (3):
    for j in range(3):
        matriz[i].append(int(input(f'Digite um número para a posição [{i},{j}]: ')))
print('-='*40)
for i in range(3):
    for j in range(3):
        print(f'[{matriz[i][j]:^5}]',end=' ')
    print('')