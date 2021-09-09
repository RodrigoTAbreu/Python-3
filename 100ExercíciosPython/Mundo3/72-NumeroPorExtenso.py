numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')
continua = ' '

while True:
    n = int(input('Digite um número: '))
    if n > 10:
        print('Digite um número de 0 a 10.')

    print(f'Você digitou {n} {numeros[n]}.')
    continua = input('Quer continuar[S/N]: ').upper()[0].strip()

    if continua == 'N':
        break


print('fim')


