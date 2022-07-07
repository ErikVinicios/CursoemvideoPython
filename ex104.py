def leiaint(n):
    while True:
        a = input(n)
        if a.isnumeric():
            return a
        else:
            print('\033[1:31mErro. Digite um número inteiro válido.\033[m')


num = leiaint('Digite um número: ')
print(f'O número digitado foi {num}')