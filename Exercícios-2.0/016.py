from math import trunc
print('='*25)
print('Mostrando porção inteira')
print('='*25)
n = float(input('Informe um número: '))
print('O Numero {} arredondando para cima é {}.'.format(n, trunc(n)))
print('Ou usando apenas um modulo interno INT {}'.format(int(n)))