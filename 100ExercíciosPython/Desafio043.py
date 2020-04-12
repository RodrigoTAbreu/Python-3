print('-='*20)
print('         CALCULANDO O IMC º|º')
print('-=' *20)
peso = float(input('Informe o peso:(kg) '))
altura = float(input(' Iforme a altura:(m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é: {:.2f}'.format(imc))

if imc <= 18.5:
    print(' Abaixo do Peso')
elif imc >= 18.5 and imc <= 24.9: #usando o operador AND para determinar uma faixa...de tanto até tanto
    print('Peso Ideal')
elif imc >= 25 and imc <= 29.9:
    print(' Sobre Peso')
elif imc >= 30 and imc <= 35.9:
    print('Obesidade Grau I')
elif 36 <= imc < 39.9: #podemos usar o teste logico antes da variavel..isso funciona apenas no PYTHON
    print('GORDO!!!!!')
elif imc >= 40:
    print('PESO MORBIDO')