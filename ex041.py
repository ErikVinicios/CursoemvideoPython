from datetime import date

anoA = int(input('Seu ano de nascimento: '))
ano = date.today()
idade = ano.year - anoA

print(f'Idade: {idade} anos')
if idade <= 9:
    categoria = '\033[1:4:36mMORIM\033[m'
elif idade <= 14:
    categoria = '\033[1:4:34mINFANTIL\033[m'
elif idade <= 19:
    categoria = '\033[1:4:39mJUNIOR\033[m'
elif idade <= 25:
    categoria = '\033[1:4:33mSÊNIOR\033[m'
else:
    categoria = '\033[1:4:31mMASTER\033[m'
print(f'Categoria: {categoria}')
