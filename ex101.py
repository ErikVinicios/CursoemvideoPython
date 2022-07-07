def voto(a):
    from datetime import date
    anoV = date.today().year - a
    if anoV < 16:
        return print(f'Com \033[1:33m{anoV} anos\033[m: VOTO \033[1:31mNÃO VOTA\033[m')
    elif anoV >= 18 and anoV < 65:
        return print(f'Com \033[1:33m{anoV} anos\033[m: VOTO \033[1:32mOBRIGATÓRIO\033[m')
    else:
        return print(f'Com \033[1:33m{anoV} anos\033[m: VOTO \033[1:34mOPCIONAL\033[m')


anoN = int(input('Digite seu ANO DE NASCIMENTO: '))
voto(anoN)
