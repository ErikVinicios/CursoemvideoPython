lista = {}
t = 0
lista['Nome'] = str(input('Nome: ')).strip().title()
qnt = int(input('Quantidade de partidas: '))
lista['Gols'] = []
for i in range(qnt):
    lista['Gols'].append(int(input(f'Gols na {i+1}ª partida: ')))
lista['Total'] = sum(lista['Gols'])
print('-='*30)
print(f'O jogador \033[1:39m{lista["Nome"]}\033[m jogou {qnt} partidas:')
for p,g in enumerate(lista['Gols']):
    print(f'    Na \033[1:32m{p+1}ª partida\033[m, fez \033[1:32m{g} gols\033[m;')
print(f'\033[1:39mTOTALIZANDO\033[m \033[1:32m{lista["Total"]} Gols\033[m')
print('-='*30)
