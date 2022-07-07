s = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'\n\033[1:32mVocê digitou \033[1:36m{c} números\033[m \033[1:32me a \033[1:35msoma entre eles é {s}.\033[m ')