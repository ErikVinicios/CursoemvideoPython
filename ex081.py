lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    alt = None
    while alt != 'S' and alt != 'N':
        alt = str(input('Deseja inserir mais números? [S/N] ')).strip().upper()
    if alt == 'N':
        break
print(f'\nLista completa: \033[1:32m{lista}\033[m')
print(f'Lista \033[1:36mORDENADA DECRESCENTE\033[m: \033[1:36m{sorted(lista,reverse=True)}\033[m')
print(f'Foram digitados \033[1:34m{len(lista)} números\033[m')
print(f'mO \033[1:33mvalor 5\033[m foi digitado \033[1:33m{lista.count(5)} vezes\033[m' if 5 in lista else "\033[1:31mNenhum valor 5 foi digitado\033[m")
