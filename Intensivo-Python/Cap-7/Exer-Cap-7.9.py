lanches = ['X-Bacon','X-Tudo','X-Calabresa', 'CalaFrango','X-Salada','CalaFrango','X-Bacon','CalaFrango']
lanches_finais = []

print('Estamos sem CalaFrango')
while 'CalaFrango' in lanches:
    lanches.remove('CalaFrango')

while lanches:
    preparo = lanches.pop()
    print('Preparei seu lanche de {}'.format(preparo))
    lanches_finais.append(preparo)
print('\nOs lanches finais hoje foram:')
for lanche in lanches_finais:
    print('\t{}'.format(lanche))