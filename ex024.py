cidade = input('Nome da cidade: ')

sep = cidade.upper().split()

print(f'O nome da cidade começa com SANTO? \033[36m{"SANTO" in sep[0]}\033[m')