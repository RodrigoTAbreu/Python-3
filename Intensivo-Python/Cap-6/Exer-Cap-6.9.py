lugares = {
    'Pedro':['Barcelona','Italia','Isarel'],
    'maria':['São Paulo'],
    'João':['Guatemala','EUA']
}
for nome, lugar in lugares.items():
    print('Para {} o melhor lugar é:'.format(nome))
    for place in lugar:
        print('\t{}'.format(place))