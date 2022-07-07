viagem = int(input('Distância da viagem em Km: '))

if viagem <= 200:
    preço = viagem * 0.5
else:
    preço = viagem * 0.45
print(f'Valor da total da viagem: \033[1:32mR${preço:.2f}\033[m. ')
