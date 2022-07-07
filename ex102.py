def fatorial(n,show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: [opcional] Mostrar ou não a conta.
    :return: O valor fatorial de um número N.
    """
    f = 1
    print('--'* 30)
    for c in range(n):
        if show:
            print(n, end='')
            if n == 1:
                print(' = ',end='')
            else:
                print(' X ', end='')
        f *= n
        n -= 1
    print(f)
    print('--'* 30)


fatorial(5, True)
help(fatorial)

