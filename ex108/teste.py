from ex108 import moeda

p = float(input('Digite um preço: R$'))
print(f'\033[1:34mA METADE de {moeda.moeda(p)}: {moeda.moeda(moeda.metade(p))}')
print(f'\033[1:35mO DOBRO de {moeda.moeda(p)}: {moeda.moeda(moeda.dobro(p))}')
print(f'\033[1:32mAUMENTANDO 10% de {moeda.moeda(p)}: {moeda.moeda(moeda.aumentar(p,10))}')
print(f'\033[1:31mREDUZINDO 13% de {moeda.moeda(p)}: {moeda.moeda(moeda.diminuir(p,13))}')