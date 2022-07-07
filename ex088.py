from random import sample
from time import sleep
lista = []
print('\033[1:37m*\033[m'*43)
print(' '*15,'\033[1:39mMEGA SENA\033[m',' '*15)
print('\033[1:37m*\033[m'*43)
qnt = int(input('Quantidade de jogos: '))
for i in range(qnt):
    lista.append(sample(range(1,61),6))
print('\033[1:37m-=\033[m'*5,f'\033[1:39mRESULTADO DOS {qnt} JOGOS\033[m','\033[1:37m-=\033[m'*5)
for i in range(qnt):
    sleep(2)
    print(f'\033[1:35mJogo {i+1}: \033[1:34m{lista[i]}\033[m')
print('-='*8,'\033[1:32mBOA SORTE\033[m','-='*8)
