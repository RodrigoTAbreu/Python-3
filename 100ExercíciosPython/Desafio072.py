extenso = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
print(len(extenso))

while True:
    numero = int(input('Informe um numero de 0 a 10:'))

    if len( extenso ) == numero:
        print( 'fim' )
        break
    else:
        print( f'Voce digitou {extenso[numero]}' )
