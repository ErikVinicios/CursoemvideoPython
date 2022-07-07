c = maior = homens = mulher20 = 0
while True:
    sexo = idade = 0
    alt = ''
    print('\n\033[1:37m---------- DADOS CADASTRAIS ----------\033[m')
    idade = int(input('idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo::[M/F]').strip().upper()
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    c += 1
    while alt != 'S' and alt != 'N':
        alt = input('\nDeseja inserir mais pessoas? [S/N]').strip().upper()
        if alt != 'S' and alt != 'N':
            print('\033[1:31mALTERNATIVA INVÁLIDA.\033[m')
    if alt == 'N':
        break
print('\n\033[1:37m--------- RESULTADOS ----------\033[m')
print(f'''\033[1:33mTOTAL DE PESSOAS: {c}
\033[1:39m{maior} possuem MAIORIDADE.
\033[1:34m{homens} são HOMENS
\033[1:36m{mulher20} são MULHER COM MENOS DE 20 ANOS\033[m''')
