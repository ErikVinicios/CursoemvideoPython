peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / altura ** 2

print(f'IMC: \033[1:4:39m{imc:.1f}\033[m')
if imc < 18.5:
    resultado = '\033[1:4:33mABAIXO DO PESO\033[m'
elif imc <= 25:
    resultado = '\033[1:4:32mPESO IDEAL\033[m'
elif imc <= 30:
    resultado = '\033[1:4:33mSOBREPESO\033[m'
elif imc <= 40:
    resultado = '\033[4:31mOBESIDADE\033[m'
else:
    resultado = '\033[1:4:31mOBESIDADE MÓRBIDA\033[m'
print(f'Resultado: {resultado}. ')