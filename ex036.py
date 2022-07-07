casa = float(input('Valor da casa: '))
salario = float(input('Seu salário: '))
tempo = int(input('Em quantos anos irá pagar: '))
parcela = casa / (tempo * 12)

print(f'\nPara pagar uma casa de \033[4:32mR${casa:.2f}\033[m em \033[4:32m{tempo} anos\033[m a prestação será de '
      f'\033[1:4:39:40mR${parcela:.2f}\033[m')
if parcela <= (30/100*salario):
    print(f'\033[1:32mEmprestimo Aprovado!\033[m ')
else:
    print(f'\033[1:31mEmprestimo Negado!\033[m ')
