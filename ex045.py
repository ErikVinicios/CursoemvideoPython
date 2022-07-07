from random import choice
from time import sleep
print('Jó...')
sleep(1)
print('Ken..')
sleep(1)
print('Po')
altP = int(input('Eu escolho...\n(1) PEDRA\n(2) PAPEL\n(3) TESOURA\n'))
print('\n'*100)
if altP == 1:
    altP = 'PEDRA'
elif altP == 2:
    altP = 'PAPEL'
else:
    altP = 'TESOURA'
altC = choice(['PEDRA','PAPEL','TESOURA'])
print(f'Eu: {altP}\nComputador: {altC}\n')

if altC == 'PEDRA' and altP == 'TESOURA' or altC == 'PAPEL' and altP == 'PEDRA' or altC == 'TESOURA' and altP == 'PAPEL':
    print('\033[1:31mEU GANHEI! VOLTE SEMPRE SEU PATINHO.\033[m ')
elif altP == altC:
    print('EMPATE! ')
else:
    print('\033[1:32mEU VENCI! VOU VENDER ESSE COMPUTADOR BURRO!\033[m ')



