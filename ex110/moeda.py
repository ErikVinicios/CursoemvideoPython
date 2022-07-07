def metade(preço, format=False):
    res = preço / 2
    return moeda(res) if format else res


def dobro(preço, format=False):
    res = preço * 2
    return moeda(res) if format else res


def aumentar(preço,porcent, format=False):
    res = preço + (porcent / 100 * preço)
    return moeda(res) if format else res


def diminuir(preço,porcent, format=False):
    res = preço - (porcent / 100 * preço)
    return moeda(res) if format else res


def moeda(preço=0,moeda='R$', format=False):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, aumento=0, desconto=0):
    print('-' * 30)
    print(f'{"RESUMO DA COMPRA":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True):}')
    print(f'{aumento}% de aumento: \t{aumentar(preço, aumento, True)}')
    print(f'{desconto}% de redução: \t{diminuir(preço, desconto, True)}')

