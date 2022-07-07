Nvelho = ''
velho = 0
soma = 0
mulher20 = 0
aux = 0
for i in range(1,5):
    print(f'=-=-= {i}ª pessoa =-=-=')
    nome = input(f'Nome:').title().strip()
    idade = int(input('Idade: '))
    soma += idade
    sexo = int(input('Sexo:\n(1) MASCULINO\n(2) FEMININO\n'))
    if idade < 20 and sexo == 2:
        mulher20 += 1
    if idade > velho and sexo == 1:
        velho = idade
        Nvelho = nome
media = soma / 4
print(f'Média das idades: {media:.1f}')
print(f'O homem mais velho é {Nvelho} com {velho} anos')
print(f'Mulheres com menos de 20 anos: {mulher20}')

