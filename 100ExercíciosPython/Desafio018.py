from math import sin, cos, tan, radians
angulo = float(input('Digite o Angulo: '))
seno = sin(radians(angulo))
print('Para o Angulo {:.2f} temos:'.format(angulo))
print('O Seno é:{:.2f}'.format(seno))
cosseno = cos(radians(angulo))
print('O Cosseno é:{:.2f}'.format(cosseno))

tang = tan(radians(angulo))
print('A Tangente é:{:.2f}'.format(tang))
