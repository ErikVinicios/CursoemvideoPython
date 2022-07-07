lista = []
for i in range(0,5):
    n = int(input('\nDigite um número: '))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print('\033[1:32mNúmero adicionado no final da lista.\033[m ')
    else:
        for p,c in enumerate(lista):
            if n <= c:
                lista.insert(p,n)
                print(f'\033[1:32mnúmero adicionado na posição \033[1:39m{p}\033[m,')
                break
print(f'\nLista completa: \033[1:36m{lista}\033[m')