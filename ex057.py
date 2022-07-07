sexo = ''
while sexo != 'M' and sexo != 'F':
    print('')
    sexo = input('Qual seu sexo? (M/F)').upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('')
        print('\033[1:31mSEXO INVÁLIDO.\033[m')
print('')
print('\033[1:32mSEXO VÁLIDO!\033[m ')