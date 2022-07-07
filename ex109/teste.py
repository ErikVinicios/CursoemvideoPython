from ex109 import moeda

p = float(input('Digite um preço: R$'))
print(f'\033[1:34mA METADE de {moeda.moeda(p)}: {moeda.metade(p, True)}')
print(f'\033[1:35mO DOBRO de {moeda.moeda(p)}: {moeda.dobro(p, True)}')
print(f'\033[1:32mAUMENTANDO 10% de {moeda.moeda(p)}: {moeda.aumentar(p,10, True)}')
print(f'\033[1:31mREDUZINDO 13% de {moeda.moeda(p)}: {moeda.diminuir(p,13, True)}')




