n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1+n2)/2

print(f'Média: \033[1:33m{m:.1f}\033[m')

if m >= 7:
    print('\033[1:32mAPROVADO\033[m')
elif m < 5:
    print('\033[1:31mREPROVADO\033[m')
else:
    print('\033[1:34mRECUPERÇÃO')
