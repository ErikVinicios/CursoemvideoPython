maior = 0
menor = 0
for c in range(1,6):
    peso = float(input(f'peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'Mais pesado: {maior} Kg')
print(f'Mais leve: {menor} Kg')


