radar = 80
vel = int(input('Velocidade: '))

if vel>radar:
    multa = (vel - radar)*7
    print(f'\033[1:31mMulta: R${multa:.2f}\033[m')
elif vel==radar:
    print('\033[1:34mVelocidade exata. \033[m')
else:
    print('\033[1:32mVelocidade permitida. \033[m')
print('\033[33mBoa Viagem! ')
