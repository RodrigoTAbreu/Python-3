from time import sleep
print('*'*20)
print('Programa TABUADA')
print('*'*20)
n = int( input( 'Digite um numero para calcular a tabuada: ' ) )

cont = result = mult = 0
while True:
    if n <= 0:
        break
    else:
        cont += 1
        result = cont * n
        print(f'{n} x {cont} = {result}')
        if cont >= 10:
            print( '*' * 20 )
            print( 'Programa TABUADA' )
            print( '*' * 20 )
            n = int( input( 'Digite um numero para calcular a tabuada: ' ) )
            cont = 0


print('OPS !! Número Negativo na Parada. Encerrando o programa.')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
print('Acabou!!!')