t = 0
c = 0
maisMIL = 0
Pbarato = 0
Nbarato = ''
while True:
    alt = ''
    print('\n\033[1:37m---------- INFORMAÇÕES DO PRODUTO ----------\033[m')
    nome = input('Nome: ').strip().title()
    preço = float(input('Preço: R$'))
    if c == 0 or Pbarato > preço:
        Pbarato = preço
        Nbarato = nome
    if preço > 1000:
        maisMIL += 1
    t += preço
    c += 1
    while alt != 'S' and alt != 'N':
        alt = input('Inserir mais produtos? [S/N] ').strip().upper()
    if alt == 'N':
        break
print('\n\033[1:37m---------- RESULTADOS DA COMPRA ----------\033[m')
print(f'''Dos {c} produtos inseridos:
\033[33m{maisMIL} produtos custam \033[1:33mMAIS DE R$1000.00\033[m
\033[34mO produto mais caro foi o(a) \033[1:34m{Nbarato}\033[34m, custando \033[1:34mR${Pbarato:.2f}
\033[mO total da compra foi R${t}.\033[m''')


