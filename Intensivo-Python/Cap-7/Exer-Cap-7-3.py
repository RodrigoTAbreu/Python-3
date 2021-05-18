numero = int(input('Informe um número: '))
if numero % 10 == 0:
    print('Você informou {}.\nEsse é um numero multiplo de 10'.format(numero))
else:
    print('Você informou {}.\nEsse não é multiplo de 10'.format(numero))
