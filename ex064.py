c = 0
s = 0
num = 0
while num != 999:
    num = int(input('Digite um número ou 999 para parar: '))
    if num != 999:
        c +=1
        s += num
print('')
print(f'\033[1:32mVocê digitou \033[1:34m{c}\033[m \033[1:32mnúmeros e a soma deles foi \033[1:36m{s}\033[m')