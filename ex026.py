frase = input('Frase: ').strip()

print(f'Quantidade de letra A: \033[31m{frase.upper().count("A")}\033[m')
print(f'Posição da primeira letra A: \033[35m{frase.upper().find("A")}\033[m')
print(f'Ultima posição da letra A: \033[34m{frase.upper().rfind("A")}\033[m')
