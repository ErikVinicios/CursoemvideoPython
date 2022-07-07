from random import randint
from time import sleep

n = randint(0,5)
num = int(input("Qual número você acha que foi sorteado?: "))
print('PROCESSANTO...')
sleep(3)
print(f"\033[1:31mO número sorteado foi: \033[4:32m{n}\033[m")
if num == n:
    print("\033[1:31mParabéns! Você acertou.\033[m")
else:
    print("\033[1:31mQUe pena! Você errou. \033[m")


