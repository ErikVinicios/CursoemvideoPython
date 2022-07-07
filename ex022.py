nome = input('Nome Completo: ')

print(f'Nome com todas as letras em MAIÚSCULASs: \033[31m{nome.upper()}\033[m')
print(f'Nome com todas as letras em MINÚSCULAS: \033[36m{nome.lower()}\033[m')
print(f'QUantidade de letras (sem espaços): \033[35m{len(nome.replace(" ",""))}\033[m')
print(f'Quantidade de letras do primeiro nome: \033[33m{nome.find(" ")}\033[m')