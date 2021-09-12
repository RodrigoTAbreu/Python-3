n = float(input('Digite um valor: '))

print('O valor digitado foi {} e sua porção inteira é {}'.format(n,int(n)))

## poderiamos usar tb a função TRUNC dentro da lib MATH
from math import trunc
n = float(input('Digite o valor: '))
print('Valor digitado {} porção inteira dele é {}'.format(n, trunc(n)))