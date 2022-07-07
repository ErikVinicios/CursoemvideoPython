def moeda(preço):
    return f'R${preço:.2f}'


def metade(preço,m=False):
    if m:
        return f'R${preço / 2:.2f}'
    return preço / 2


def dobro(preço,m=False):
    if m:
        return f'R${preço * 2:.2f}'
    return preço * 2


def aumentar(preço,porcent,m=False):
    if m:
        return f'R${(porcent / 100 * preço) + preço:.2f}'
    return (porcent / 100 * preço) + preço


def diminuir(preço,porcent,m=False):
    if m:
        return f'R${preço - (porcent / 100 * preço):.2f}'
    return preço - (porcent / 100 * preço)


def resumo(preço, aumento=0, desconto=0):
    print('-' * 40)
    print(f'{"RESUMO DA COMPRA":^40}')
    print('-' * 40)
    print(f'Preço analisado: R${preço:.2f}')
    print(f'Dobro do preço: R${preço * 2:.2f}')
    print(f'Metade do preço: R${preço / 2:.2f}')
    print(f'{aumento}% de aumento: R${preço + (aumento / 100 * preço):.2f}')
    print(f'{desconto}% de redução: R${preço - (aumento / 100 * preço):.2f}')
