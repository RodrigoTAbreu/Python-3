from random import randint

def sorteia(lista):
    n = 0
    while n <= 4:
        num = randint(1, 10)
        lista.append(num)
        n += 1
    print(valores)


def pares(lista):
    par = 0
    for c in lista:
        if c % 2 == 0:
            par += c
    print(par)

valores = list()
sorteia(valores)
pares(valores)
