from math import hypot
print('='*25)
print('Calculando a Hipotenusa')
print('='*25)
ca = float(input('Informe o Cateto Adjacente: '))
co = float(input('Informe o Cateto Oposto: '))
n = hypot(ca,co)
print('A Hipotenusa é {:.2f}'.format(n))