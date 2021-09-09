numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')
continua = ' '

while True:
    n = int(input('Digite um número: '))
    while n not in range(0,10):
        if n > 10:
            print('Digite um número de 0 a 10.')
            n = int(input('Digite um número: '))
    if n < 10:
        print(f'Você digitou {n} {numeros[n]}.')

    while continua not in 'SN':
        continua = input('Quer continuar[S/N]: ').upper()[0].strip()

    if continua == 'N':
        break

print('fim')


