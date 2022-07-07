from random import randint
tupla = (randint(0,20),randint(0,20),randint(0,20),randint(0,20),randint(0,20))
maior = max(tupla)
menor = min(tupla)
print(f'Números sorteados: \033[1:32m{tupla}\033[m')
print(f'O maior número: \033[1:36m{maior}\033[m')
print(f'O menor número: \033[1:35m{menor}\033[m')