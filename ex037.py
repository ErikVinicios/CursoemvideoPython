num = int(input('Digite um número: '))
alt = int(input('Qual será a base de conversão?\n(1) Binário\n(2) Octal\n(3) Hexadecimal\n'))

if alt == 1:
    converção = bin(num)
    nome = 'BINÁRIO'
elif alt == 2:
    converção = oct(num)
    nome = 'OCTAL'
else:
    converção = hex(num)
    nome = 'HEXADECIMAL'
print(f'A converção do número \033[1:32m{num}\033[m em \033[1:32m{nome}\033[m é \033[4:36m{converção[2:]}\033[m. ')
