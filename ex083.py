lista = []
contP = []
lista.extend(input('Digite uma expressão: '))
for c in lista:
    if c == '(':
        contP.append('(')
    elif c == ')':
        if len(contP) > 0:
            contP.pop()
        else:
            contP.append(')')
print('\033[1:32mExpressão Válida!\033[m' if len(contP) == 0 else '\033[1:31mExpressão Inválida.\033[m')
