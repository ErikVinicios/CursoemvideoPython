from math import trunc

num = float(input('Digite um número: '))

print(f"O número \033[32m{num}\033[m tem a tem a parte inteira \033[36m{trunc(num)}")