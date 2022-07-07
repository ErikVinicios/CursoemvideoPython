from datetime import date

ano = int(input('Digite um ano ou 0 para inserir o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[1:35m{ano}\033[m é um ano bissexto. ')
else:
    print(f'\033[35m{ano}\033[m não é um ano bissexto. ')
