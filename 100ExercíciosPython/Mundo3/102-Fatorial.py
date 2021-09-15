def fatorial(numero,show=True):
    '''
    --> Calcula o Fatorial de um número:
    :param n: O número  a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    '''
    from math import factorial
    from time import sleep
    #numero = int(input('Informe um número: '))
    print('Calculando o Fatorial.',end='')
    sleep(1)
    print('.',end='')
    sleep(0.5)
    print('.')
    fatnum = numero
    fatorial = 1 # iniciada com 1 apenas se for calcular o fatorial manualmente.
    if show == False:
        fatorial = factorial( numero )
        # fatorial *= fatnum #calcula o fatorial manual porem a variavel deve iniciar com 1
        fatnum -= 1
        print(fatorial)
    if show == True:
        while fatnum > 0:
            print('{}'.format(fatnum),end='')

            print(' x 'if fatnum > 1 else ' = ',end='') # imprime X se fatnum>1, senão imprime =
            fatorial = factorial(numero)
            #fatorial *= fatnum #calcula o fatorial manual porem a variavel deve iniciar com 1
            fatnum -= 1

        print('{}'.format(fatorial))


fatorial(5)
fatorial(5, False)