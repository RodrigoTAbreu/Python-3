print('=='*25)
print('Calulando a área de uma parede.')
print('=='*25)

altura = float(input('Informe a Altura: '))
larg = float(input('Informe a Largura: '))
res = altura * larg
tinta = res / 2
print('A área calculada é {:.1f}m2.'.format(res))
print('Você vai precisar de {:.1f} litros de tinta.'.format(tinta))
