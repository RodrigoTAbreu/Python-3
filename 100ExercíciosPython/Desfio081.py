lista = []
b = 5
while True:
    lista.append( int(input( 'Digite o valor: ' ) ))
    resp = str( input( 'Deseja continuar ? [S/N]: ' ) ).upper().strip()[0]
    if resp in 'Nn':
        break
print( f'Foram digitados {len(lista)} numeros' )
lista.sort( reverse=True )
print( f'A lista em ordem decrescente {lista} ' )
if 5 in lista:
    print('Cinco foi inserido na lista' )
else:
    print('O numero cinco não foi inserido' )

