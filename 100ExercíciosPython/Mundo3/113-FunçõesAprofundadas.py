def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um número INTEIRO válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mO Usuário interrompeu a execução.\033[m')
            return 0
        else:
            return n


def leiaReal(msg):
    while True:
        try:
            r = float(input(msg))
        except (ValueError,TypeError):
            print('\033[0;31mERRO: Digite um número REAL válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mO Usuário interrompeu a execução.\033[m')
            return 0
        else:
            return r

n1 = leiaint('Digite um Número INTEIRO: ')
n2 = leiaReal('Digite um Número REAL: ')
print(f'O valor INTEIRO digital foi {n1} e o valor REAL foi {n2}')


