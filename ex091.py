from random import randint
from time import sleep
from operator import itemgetter
dados = {}
rank = []
for i in range(1,5):
    dados[f'Jogador {i}'] = randint(1,6)
print('-='*6,'SORTEIO','-='*6)
for k,v in dados.items():
    sleep(2)
    print(f'O {k} sorteou o número {v}')
print('-='*6,'RANKING','-='*6)
rank = sorted(dados.items(), key=itemgetter(1),reverse=True)
for i,v in enumerate(rank):
    sleep(2)
    print(f'{i+1}ª posição: {v[0]} com {v[1]}')
