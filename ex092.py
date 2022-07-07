from datetime import date
dados = {}
dados['Nome'] = str(input('Nome: ')).strip().title()
anoN = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - anoN
dados['ctps'] = int(input('Carteira de trabalho [0 não tem]: '))
if dados['ctps'] == 0:
    print('-='*30)
    for k,v in dados.items():
        print(f'\033[1:33m{k}\033[m: \033[1:39m{v}\033[m')
else:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = int(input('Salário: R$'))
    dados['Aposentadoria'] = (dados['contratação'] + 35) - anoN
    print('-=' * 30)
    for k,v in dados.items():
        print(f'\033[1:33m{k}\033[m: \033[1:39m{v}\033[m')
    print('-='*30)
