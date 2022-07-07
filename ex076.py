listagem = ('Arroz',15,
            'Feijão',10
            ,'Macarrão',2
            ,'Carne',25)
print(f'{"LISTAGEM DE PREÇOS":^40}')
for c in range(0,len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<33}',end='')
    else:
        print(f'R${listagem[c]:>5.2f}')
