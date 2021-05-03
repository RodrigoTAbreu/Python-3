import math
print('='*35)
print('Valor de Seno, CosSeno e Tangente')
print('='*35)
n = float(input('Qual é o angulo ?: '))
print('O Valor de Seno é {:.2f} \n O Cosseno é {:.2f} \n A Tangente é {:.2f}'.format(math.sin(math.radians(n)),math.cos(math.radians(n)),math.tan(math.radians(n))))
