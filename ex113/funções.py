def leiaint(msg):
    while True:
        try:
            a = int(input((msg)))
        except ValueError:
            print('\033[1:31mERRO: O número digitado não é INTEIRO. Tente novamente...\033[m ')
        except KeyboardInterrupt:
            print('\033[1:31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return a

def leiafloat(msg):
    while True:
        try:
            a = float(input(msg))
        except ValueError:
            print('\033[1:31mERRO: O número digitado não é REAL. Tente novamente...\033[m ')
        except KeyboardInterrupt:
            print('\033[1:31mO usuário escolheu não digitar um valor REAL.\033[m ')
            return 0
        else:
            return a