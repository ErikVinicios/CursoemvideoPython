frase = input('Frase: ').strip().upper().replace(' ','')
fraseA = frase[::-1]
print(f'A frase {frase} invertida fica {fraseA}')
if frase == fraseA:
    print('\033[1:4:32mPalindromo! \033[m')
else:
    print('\033[1:4:31mNão é um palindromo. \033[m')