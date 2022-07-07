def leiaint(msg):
    while True:
        try:
            a = int(input(msg))
        except ValueError:
            print('\033[1:31mERRO: Digite um número INTEIRO.\033[m ')
        else:
            return a


def lerarquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
    print('-' * 40)
    print(texto)


def editararquivo(arquivo,nome,idade=0):
    with open(arquivo, 'a') as arquivo:
        arquivo.write(f'\n{nome:<20} \t\t{idade} anos')
    print(f'Registro de {nome} adicionado. ')

