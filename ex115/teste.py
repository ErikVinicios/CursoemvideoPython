from ex115 import funções

while True:
    alt = None
    while True:
        print('-' * 40)
        print(f'{"MENU PRINCIPAL":^40}')
        print('-' * 40)
        alt = int(input('''Escolha uma opção:
[\033[1:33m1\033[m] \033[1:34mVER PESSOAS CADASTRADAS\033[m
[\033[1:33m2\033[m] \033[1:34mCADASTRAR NOVA PESSOA\033[m
[\033[1:33m3\033[m] \033[1:34mSAIR DO SISTEMA\033[m

\033[1:33mSua resposta:\033[m '''))
        if alt == 1 or alt == 2 or alt == 3:
            break
        else:
            print('\033[1:31mERRo. Digite uma alternativa válida.\033[m')
    if alt == 1:
        funções.lerarquivo('ex115.txt')
    elif alt == 2:
        print('-' * 40)
        print(f'{"NOVO CADASTRO":^40}')
        print('-' * 40)
        n = input('Nome: ').strip().title()
        i = funções.leiaint('Idade: ')
        funções.editararquivo('ex115.txt', n, i)
    elif alt == 3:
        print('-' * 40)
        print('VOLTE SEMPRE! ')
        print('-' * 40)
        break