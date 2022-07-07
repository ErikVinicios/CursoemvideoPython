def ficha(n,g):
    if n == '':
        n = '<desconhecido>'
    if g.isnumeric():
        int(g)
    else:
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input('Nome: ')).strip().title()
gols = str(input('Quantidade de gols: '))
ficha(nome, gols)
