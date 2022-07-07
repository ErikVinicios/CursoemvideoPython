nome = input('Nome Completo: ')

print(f'Este nome possui SILVA? \033[33m{"SILVA" in nome.upper().split()}\033[m ')