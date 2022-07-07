lista = []
listaM = []
listaME = []
dados = {}
s = m = 0
while True:
    dados['Nome'] = str(input('Nome: ')).strip().upper()
    dados['Sexo'] = None
    while dados['Sexo'] != 'M' and dados['Sexo'] != 'F':
        dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()
    dados['Idade'] = int(input('Idade: '))
    s += dados['Idade']
    if dados['Sexo'] == 'F':
        listaM.append(dados["Nome"])
    lista.append(dados.copy())
    alt = None
    while alt != 'S' and alt != 'N':
        alt = str(input('Deseja inserir mais pessoas? [S/N] ')).strip().upper()
    if alt == 'N':
        break
m = s/len(lista)
for i in lista:
    if i['Idade'] >= m:
        listaME.append(i)
print('-='*30)
print(f'''Foram cadastradas \033[1:39m{len(lista)} PESSOAS\033[m;
A \033[1:32mMÉDIA DAS IDADES\033[m é \033[1:32m{m:.2f}\033[m;
Lista com \033[1:35mTODAS AS MULHERES\033[m: \033[1:35m{listaM}\033[m;
Lista com as \033[1:34mPESSOAS MAIS VELHAS\033[m: \033[1:34m{listaME}\033[m.''')
