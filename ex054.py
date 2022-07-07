from datetime import date
maior = 0
menor = 0
for c in range(1,8):
    anoN = int(input(f'{c}ª pessoa: Ano de nascimento: '))
    idade = date.today().year - anoN
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas atingiram a maioridade e {menor} pessoas ainda não atingiram a maioridade. ')