print('='*42)
print('           TIPOS DE TRIÂNGULO')
print('='*42)
a = float(input('Informe o Lado A:'))
b = float(input('Informe o Lado B:'))
c = float(input('Informe o Lado C:'))

if a + b > c and a + c > b and c + b > a:
    print('Formam um triangulo: ', end='')
    if a == b == c:
        print('EQUILATETO')
    elif a != b != c != a :
        print('ESCALENO')
    else:
        print('ISOSCELES')

else:
    print('Não formam um triangulo')
