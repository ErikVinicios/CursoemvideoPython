nome = input('Nome Completo: ').strip()

sep = nome.split()

print(f'Primeiro nome: \033[33m{sep[0]}\033[m\nUltimo nome: \033[34m{sep[-1]}\033[m ')