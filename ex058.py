from random import randint
numC = randint(0,10)
print('\033[1:31mUm número entre 0 e 10 foi sorteado. Tente adivinhar qual foi.\033[m')
c = 1
num = 11
while num != numC:
    print('')
    num = int(input('\033[1:36mO número sorteado foi:\033[m '))
    if num != numC:
        if num > numC:
            print('')
            print('\033[1:31mMENOS... Tente novamente.\033[m')
        else:
            print('')
            print('\033[1:31mMAIS... Tente novamente.\033[m')
        c += 1
print('')
print(f'\033[1:32mPARABÉNS! Você acertou!\033[m\nTentativas: \033[1:39m{c}\033[m')

