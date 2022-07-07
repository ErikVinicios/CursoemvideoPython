s = 0
cont = 0
for c in range(1,7):
    n = int(input(f'{c}º número: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Você informou {cont} números pares e a soma deles é {s}')
print('FIM! ')