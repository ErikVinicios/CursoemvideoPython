from math import hypot

CO = float(input('Cateto oposto: '))
CA = float(input('Cateto adjacente: '))

print(f'O comprimento da hipotenusa é \033[32m{hypot(CO,CA):.2f}\033[m')
