peso = float(input('Informe o Peso: '))
altura = float(input('Informe a Altura: '))
imc = peso / (altura*altura)

print('Seu peso atual é {}Kg'.format(peso))
print('Sua Altura é {}Mt'.format(altura))
print('Seu IMC está em {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif 25 > imc > 18.5:
    print('Seu peso é o ideal.')
elif 30 > imc > 25:
    print('Você esá com sobrepeso.')
elif 40 > imc > 30:
    print('Você está Obeso.')
elif imc > 40:
    print('Você é um OBESO MORBIDO.')



