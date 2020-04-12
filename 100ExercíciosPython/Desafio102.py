from math import factorial

def fatorial(n, show = False):
    """
    -->>Calculo do Fatorial de un número já pré-definido.
    :param n:Número a ser calculado.
    :param show:(Opicional) Mostra ou não o Calculo realizado.
    :return:O valor do fatorial de um número
    """
    c = 1
    fat = factorial(n)
    print(f'O Valor de FAT é: {fat}')
    if show == True:
        print(f'{n}', end='')
        for c in range(n-1,0, -1):
            print(f' x {c} ',end='')
            c +=1
        print(f'= {fat}')

print('=='*25)
fatorial(10, True)
print('=='*25)
help(fatorial)
print('=='*25)