dados = {}
lista = []
while True:
    dados['Nome'] = str(input('Nome: ')).strip().title()
    qnt = int(input('Quantidade de jogos: '))
    dados['Gols'] = []
    for i in range(qnt):
        dados['Gols'].append(int(input(f'Gols no jogo {i+1}: ')))
    dados['Total'] = sum(dados['Gols'])
    lista.append(dados.copy())
    alt = None
    while alt != 'S' and alt != 'N':
        alt = str(input('Deseja inserir mais jogadores [S/N]? ')).strip().upper()
        print('-=' * 30)
    if alt == 'N':
        break
print('| CÓDIGO |          NOME          |      GOLS      |   TOTAL   |')
for p,d in enumerate(lista):
    print(f'!{p:^8}|{d["Nome"]:^24}|{str(d["Gols"]):^16}|{d["Total"]:^11}|')
print('-='*30)
while True:
    opt = int(input('Mostrar dados de qual jogador [999 para sair] ? '))
    if opt == 999:
        break
    elif opt >= len(lista):
        print('\033[1:31mERRO! Jogador não encontrado. Tente novamente.\033[m')
        print('-=' * 30)
    else:
        print('-=' * 30)
        print(f'LEVANTAMENTO do jogador {lista[opt]["Nome"]}')
        for p,d in enumerate(lista[opt]["Gols"]):
            print(f'No {p+1}º jogo fez {d} gols;')
        print('-=' * 30)
