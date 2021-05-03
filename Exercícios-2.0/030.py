numero = int(input('Digite um número: '))
par = numero % 2
if par == 1:
    print('O Número {} é IMPAR.'.format(numero))
else:
    print('O número {} é PAR.'.format(numero))
