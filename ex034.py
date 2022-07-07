sal = float(input('Salário: R$'))

if sal > 1250:
    aumento = 10/100*sal
else:
    aumento = 15/100*sal
print(f'Aumento: \033[1:32mR${aumento:.2f}\033[m')
print(f'Quem ganha \033[32mR${sal:.2f}\033[m passará a ganhar \033[1:4:32mR${sal+aumento:.2f}')