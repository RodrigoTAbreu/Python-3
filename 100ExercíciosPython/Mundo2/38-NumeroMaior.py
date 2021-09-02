numeroA = int(input('Informe 1º número: '))
numeroB = int(input('Informe 2º número: '))

if numeroA > numeroB:
    print('O primeiro é maior.'.format(numeroA))
elif numeroB > numeroA:
    print('O segundo é maior.'.format(numeroB))
else:
    print('Os números são iguais')
