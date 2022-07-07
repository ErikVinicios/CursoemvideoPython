lista = []
listaP = []
listaL = []
maior = menor = 0
dados = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    lista.append(dados[:])
    dados.clear()
    alt = None
    while alt != 'S' and alt != 'N':
        alt = str(input('Deseja inserir mais pesoas? [S/N] ')).strip().upper()
    if alt == 'N':
        break
maior = lista[0][1]
menor = lista[0][1]
for p in lista:
    if p[1] > maior:
        listaP.clear()
        maior = p[1]
        listaP.append(p[0])
    elif p[1] == maior:
        listaP.append(p[0])
    if p[1] < menor:
        listaL.clear()
        menor = p[1]
        listaL.append(p[0])
    elif p[1] == menor:
        listaL.append(p[0])
print('')
print('-='*40)
print(f'''\033[1:32mForam inseridas \033[1:36m{len(lista)} pessoas\033[m;
\033[1:32mLista completa: \033[1:39m{lista}\033[m;
\033[1:32mO \033[1:31mMAIOR PESO\033[1:32m foi \033[1:31m{maior}Kg, de \033[1:31m{listaP}\033[m;
\033[1:32mO \033[1:34mMENOR PESO\033[1:32m foi \033[1:34m{menor}Kg, de \033[1:34m{listaL}\033[m.''')