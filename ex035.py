r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r3 < r1 + r2 and r2 < r1 * r3 and r1 < r2 * r3:
    print('\033[1:32mÉ possível formar um triãngulo.\033[m ')
else:
    print('\033[31mNão é possível formar um triãngulo. \033[m')
