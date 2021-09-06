peso = float(input('Digite seu peso[kg]: '))
altura = float(input('Digite a sua altura [MT]: '))
imc = (peso/altura)**2
print(imc)

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 25 > imc > 18.5:
    print('Seu peso está dentro do IDEAL')
elif 30 > imc > 25:
    print('Você está com SOBREPESO.')
elif 40 > imc >30:
    print('Atenção. Você está OBESO!!!')
elif imc > 40:
    print('Você está com obesidade MORBIDA !!!!')

