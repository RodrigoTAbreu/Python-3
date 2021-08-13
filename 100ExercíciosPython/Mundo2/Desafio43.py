print('-------Calculando o IMC-------')
peso = float(input('Informe o PESO [Kg]: '))
altura = float(input('Informe a Altura [Mt]: '))
imc = peso / (altura*altura)
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('MAGREZA')
elif imc >=18.5 and imc <24.9:
    print('NORMAL')
elif imc >=25 and imc <29.9:
    print('SOBREPESO')
elif imc >=30 and imc < 39.9:
    print('OBESO')
elif imc >=40:
    print('MORBIDO')
