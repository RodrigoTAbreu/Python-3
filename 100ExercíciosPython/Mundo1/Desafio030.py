import math
n = int(input('Informe um valor inteiro: '))
d = n.__divmod__(n)
if n % 2 == 0:
    print('Esse número é par')
else:
    print('Esse número é impar')

#outro modo
resultado = n % 2
if resultado == 0:
    print('Esse numero é par')
else:
    print('Esse numero é impar')