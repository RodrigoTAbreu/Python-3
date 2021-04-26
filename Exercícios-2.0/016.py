import math
print('='*35)
print('Lendo parte inteira de um número')
print('='*35)
n = float(input('Digite um número quebrado: '))
res = math.floor(n)
print('A parte inteira para menos de {} é {}.'.format(n,res))
print('A parte inteira para maior de {} é {}.'.format(n, math.ceil(n)))