n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))

if n1 > n2:
    print(f'\nO \033[4:32m1º número\033[m é maior. ')
elif n2 > n1:
    print(f'\nO \033[4:32m2º número\033[m é maior. ')
else:
    print('\n\033[1:32mAmbos os números são iguais\033[m. ')
