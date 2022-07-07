from ex107 import moeda

p = float(input('Digite um preço: R$'))
print(f'\033[1:34mA METADE de R${p:.2f}: R${moeda.metade(p):.2f}')
print(f'\033[1:35mO DOBRO de R${p:.2f}: R${moeda.dobro(p):.2f}')
print(f'\033[1:32mAUMENTANDO 10% de R${p:.2f}: R${moeda.aumentar(p,10):.2f}')
print(f'\033[1:31mREDUZINDO 13% de R%{p:.2f}: R${moeda.diminuir(p,13):.2f}')