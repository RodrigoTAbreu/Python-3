from random import randint

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0,5):
        num = randint(1, 10)
        lista.append(num)
        print(f'{num} ', end='')
    print('PRONTO')


def pares(lista):
    par = 0
    for c in lista:
        if c % 2 == 0:
            par += c
    print(F'Somando os valorees pares, o total é: {par}')

valores = list()
sorteia(valores)
pares(valores)
