preço = float(input('Valor do produto: R$'))
alt = int(input('Forma de pagamento:\n(1) Á vista no dinheiro/cheque\n(2) Á vista no cartão\n(3) 2x no cartão\n'
                '(4) 3x ou mais no cartão\nSua opção: '))
if alt == 1:
    pagar = preço - (10 / 100 * preço)
    print(f'Desconto: \033[1:4:32mR${10 / 100 * preço:.2f}\033[m')
elif alt == 2:
    pagar = preço - (5 / 100 * preço)
    print(f'Desconto: \033[1:4:32mR${5 / 100 * preço:.2f}\033[m')
elif alt == 3:
    pagar = preço
    print(f'Parcela: \033[1:32mR${pagar / 2:.2f}\033[m')
else:
    parcela = int(input('Quantas parcelas? '))
    print(f'Juros: \033[5:31mR${20 / 100 * preço:.2f}\033[m')
    pagar = preço + (20 / 100 * preço)
    print(f'Parcelas: \033[1:32mR${pagar / parcela:.2f}\033[m')
print(f'Valor total: \033[1:4:39:40mR${pagar:.2f}\033[m')

