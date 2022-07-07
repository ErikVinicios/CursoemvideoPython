from random import choice

n1 = input('Digite o 1º nome: ')
n2 = input('Digite o 2º nome: ')
n3 = input('Digite o 3º nome: ')
n4 = input('Digite o 4º nome: ')
aluno = choice([n1,n2,n3,n4])

print(f'O aluno escolhido foi \033[4:36m{aluno}\033[m')