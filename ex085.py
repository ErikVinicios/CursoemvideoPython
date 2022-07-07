lista = [[],[]]
for c in range(7):
    n = int(input('Digite um valor: '))
    lista[0].append(n) if n % 2 == 0 else lista[1].append(n)
print('-='*40)
print(f'\033[1:32mOs valores \033[1:33mPARES \033[1:32mdigitados foram: \033[1:33m{sorted(lista[0])}\033[m')
print(f'\033[1:32mOs valores \033[1:36mIMPARES \033[1:32mdigitados foram: \033[1:36m{sorted(lista[1])}\033[m')