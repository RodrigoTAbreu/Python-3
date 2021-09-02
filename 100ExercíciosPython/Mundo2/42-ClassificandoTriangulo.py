r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1+r3 and r3 < r2 + r1:
    print('Esses valores formam um Triangulo')
    if r1 != r2 and r1!= r3 and r3 != r2:
        print('Triangulo ESCALENO')
    elif r1 == r2 == r3:
        print('Triangulo EQUILÁTERO')
    else:
        print('Triangulo ISÓSCELES')
else:
    print('Esses valores não formam um triangulo')
