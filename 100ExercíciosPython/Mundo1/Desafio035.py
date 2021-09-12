r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1+r3 and r3 < r2 + r1:
    print('Esses valores formam um Triangulo')
else:
    print('Esses valores não formam um triangulo')
