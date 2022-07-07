def leiaDinheiro(frase):
    while True:
        a = input(frase).replace(',', '.').strip()
        if a.isalpha() == False and a.isspace() == False and a.strip() != '':
            a = float(a)
            return a
        print(f'\033[1:31mERRO: "{a}" é um preço inválido.\033[m')
