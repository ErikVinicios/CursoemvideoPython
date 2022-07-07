a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))

if a < b * c and b < a * c and c < a * b:
    if a == b == c:
        tipo = 'EQUILÁTERO'
    elif a == b or a == c or b == c:
        tipo = 'ÍSÓSCELES'
    else:
        tipo = 'ESCALENO'
    print(f'\033[1:32mé possível montar um triangulo \033[1:4:32m{tipo}\033[m.')
else:
    print('\033[1:31mNão é possivel formar um triangulo. ')