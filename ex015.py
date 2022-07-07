km = float(input('Quilometros percorridos: '))
dias = int(input('Dias alugados: '))
taxa = (km * 0.15) + (dias * 60)

print(f'Taxa a pagar: \033[1:30:47mR${taxa:.2f}\033[m')