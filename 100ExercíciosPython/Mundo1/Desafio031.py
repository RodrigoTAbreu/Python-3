dist = float(input('Informe a distancia (km) da Viagem: '))
if dist <= 200:
    valor = dist *0.50
    print('O valor da passagem é {}'.format(valor))
else:
    valor = dist * 0.45
    print('O valor da passagem é {}'.format(valor))
