print('------ TIPO DE TRIANGULO -----')

reta1 = int(input('Informe o valor da primeira reta: '))
reta2 = int(input('Informe o valor da segunda reta: '))
reta3 = int(input('Informe o valor da terceira reta: '))

if reta1 < reta2+reta3 and reta2<reta1+reta3 and reta3<reta1+reta2:
    print('Temos um triangulo')
    if reta1 == reta2 == reta3:
        print('E é um triângulo EQUILÁTERO')
    elif reta1 != reta2 != reta3:
        print('E é um triângulo ESCALENO')
    else:
        print('E é um triângulo ISÓSCELES')
else:
    print('Não temos um triangulo')

