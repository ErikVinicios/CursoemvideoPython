def notas(*num, sit=False):
    """
    -= Função para analisar notas e situações de vários alunos.
    :param num: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    total = soma = maior = menor = media = 0
    situação = ''
    for p,c in enumerate(num):
        total += 1
        if p == 0:
            maior = c
            menor = c
        if c > maior:
            maior = c
        if c < menor:
            menor = c
        soma += c
    media = soma / total
    if sit:
        if media > 7:
            situação = 'Boa'
        elif media < 4:
            situação = 'Ruim'
        else:
            situação = 'Normal'
        geral = {'Total': total, 'Maior': maior, 'Menor': menor, 'Média': media, 'Situação': situação}
        return geral
    geral = {'Total': total, 'Maior': maior, 'Menor': menor, 'Média': media}
    return geral


resp = notas(5.5, 9.5, 10, 6.5, 10, 8, sit=True)
print(resp)
help(notas)