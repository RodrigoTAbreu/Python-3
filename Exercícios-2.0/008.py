print('=='*25)
print('Conversão de Metros x Centímetros x Milímetros')
print('=='*25)

metro = float(input('Informe o valor em Metros (Mt): '))
resmt = metro * 100
resmm = metro * 1000
print('Para {} metros você terá \n {} centímetros e \n {} milímetros.'.format(metro, resmt, resmm))