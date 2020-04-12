from math import hypot
co = float(input('Informe o Cateto Oposto: '))
ca = float(input('Informe o Cateto Adjacente: '))
print('Para Cateto Oposto {} e Cateto Adjacente {} a hipotenusa é {:.2f}'.format(co, ca,hypot(co,ca)))