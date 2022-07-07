def metade(preço):
    res = preço / 2
    return res


def dobro(preço):
    res = preço * 2
    return res


def aumentar(preço,porcent):
    res = preço + (porcent / 100 * preço)
    return res


def diminuir(preço,porcent):
    res = preço - (porcent / 100 * preço)
    return res


def moeda(preço=0,moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
