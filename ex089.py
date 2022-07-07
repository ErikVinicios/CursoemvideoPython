dados = []
lista = []
while True:
    dados.append(str(input('Nome: ')).title().strip())
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    dados.append((dados[1]+dados[2])/2)
    lista.append(dados[:])
    dados.clear()
    alt = None
    while alt != 'S' and alt != 'N':
        alt = str(input('Deseja inserir mais alunos? [S/N] ')).strip().upper()
    if alt == 'N':
        break
print('='*40)
print('\033[1:37mNúmero\033[m |      \033[1:39mNOME\033[m      |    \033[1:36mMÉDIA\033[m    |')
for p,i in enumerate(lista):
    print(f'\033[1:37m{p:^7}\033[m|\033[1:39m{i[0]:^16}\033[m|\033[1:36m{i[3]:^13.1f}\033[m|')
print('='*40)
while True:
    opt = None
    opt = int(input('Deseja mostrar a nota de qual aluno? \033[1:31m[999 para sair]\033[m '))
    if opt == 999:
        print('\n\033[1:32mPROGRAMA FINALIZADO.\033[m')
        break
    else:
        print(f'\033[1:32mAs notas de \033[1:39m{lista[opt][0]}\033[1:32m foram: \033[1:36m{lista[opt][1]}\033[m \033[1:32me \033[1:36m{lista[opt][2]}\033[m')
        print('=' * 40)
