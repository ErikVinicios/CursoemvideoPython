from datetime import date

sexo = int(input('Você é:\n(1) HOMEM\n(2) MULHER\nResposta: '))
if sexo == 1:
    anoN = int(input('Digite seu ano de nascimento: '))
    anoA = date.today().year
    idade = anoA - anoN

    if idade < 18:
        alistamento = 18 - idade
        print(f'\n\033[1:31mFalta {alistamento} ano(s) para seu alistamento. \033[m'
            f'\n\033[1:31mVocê terá que se alistar em \033[1:4:31m{anoA+alistamento}\033[m ')
    elif idade > 18:
        alistamento = idade - 18
        print(f'\n\033[1:31mPassou {alistamento} ano(s) da data do seu alistamento. \033[m'
            f'\n\033[1:31mVocê deveria ter se alistado em \033[1:4:31m{anoA-alistamento}\033[m')
    else:
        print(f'\n\033[1:32mVocê possui 18 anos e deverá se alistar IMEDIATAMENTE. \033[m. ')
else:
    print('\033[1:32mMulheres não precisam se alistar.\033[m ')