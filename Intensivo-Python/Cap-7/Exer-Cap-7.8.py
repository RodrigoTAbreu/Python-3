lanches = ['X-Bacon','X-Tudo','X-Calabresa', 'CalaFrango','X-Salada']
lanches_finais = []

while lanches:
    preparo = lanches.pop()
    print('Preparei seu lanche de {}'.format(preparo))
    lanches_finais.append(preparo)
print('\nOs lanches finais hoje foram:')
for lanche in lanches_finais:
    print('\t{}'.format(lanche))