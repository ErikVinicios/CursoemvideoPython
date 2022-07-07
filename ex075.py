tupla = (int(input(f'1º número: ')),
         int(input(f'2º número: ')),
         int(input(f'3º número: ')),
         int(input(f'4º número: ')))
print(f'Tupla: {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes. ' if 9 in tupla else 'O número 9 não apareceu nenhuma vez.')
print(f'O primeiro valor 3 aparece na {tupla.index(3)+1}º posição. ' if 3 in tupla else 'Nenhum 3 não foi inserido.')
print(f'Os números pares dessa tupla são ',end = ' ')
for num in tupla:
    if num % 2 == 0:
        print(num,end = ' ')