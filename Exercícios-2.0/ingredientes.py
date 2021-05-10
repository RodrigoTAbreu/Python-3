ingredientes = ['tomate seco','catupiry','cheder', 'palmito']
verificar = input('Consulte o ingrediente: ')
if verificar in ingredientes:
    print('Temos isso sim')
else:
    print('Precisamos comprar {}'.format(verificar))