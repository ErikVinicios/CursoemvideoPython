lista = []
listaPAR = []
listaIMPAR = []
while True:
    lista.append(int(input('Digite um número: ')))
    alt = None
    while alt != 'S' and alt != 'N':
        alt = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if alt == 'N':
        break
for c in lista:
    listaPAR.append(c) if c % 2 == 0 else listaIMPAR.append(c)
print('-+'*40)
print(f'Lista: \033[1:34m{lista}\033[m')
print(f'Lista dos números \033[1:31mPARES\033[m: \033[1:31m{listaPAR}\033[m')
print(f'Lista dos números \033[1:36mIMPARES\033[m: \033[1:36m{listaIMPAR}\033[m')