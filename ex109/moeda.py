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


def moeda(preço=0,moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
