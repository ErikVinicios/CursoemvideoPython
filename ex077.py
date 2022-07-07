palavras = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON',
            'CURSO','GRATIS','ESTUDAR','PRATICAR')
for palavra in palavras:
    print(f'\nAs vogais da palavra {palavra} são ',end = '')
    for letra in palavra:
        if letra in 'AEIOU':
            print(f'{letra} ', end = '' )
