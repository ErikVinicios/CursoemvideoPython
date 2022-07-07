preco = float(input('Preço atual do produto: R$'))

print(f'Novo preço: \033[1;32;40mR${preco-(5/100*preco):.2f}\033[m')