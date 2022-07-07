lista = []
while True:
    n = int(input(' Digite um valor: '))
    lista.append(n) if n not in lista else print("\033[1:31mEsse número ja está na lista.\033[m")
    alt = None
    while alt != 'S' and alt != 'N':
        alt = str(input('Deseja inserir mais valoes? [S/N]')).upper().strip()
    if alt == 'N':
        break
print(f'\nLista completa: \033[1:36m{sorted(lista)}\033[m')