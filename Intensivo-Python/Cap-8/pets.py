'''def descricao_pet(tipo, name):
    Exibe informações sobre um animal de  estimação.
    print('\nEu tenho um(a){}'.format(tipo).upper())
    print('O nome do meu {} é {}.'.format(tipo,name).title())
descricao_pet('peixe','aquaman')
descricao_pet('hamster','mouse')
descricao_pet(tipo='dog', name='cat')'''

def descricao_pet(name, tipo='fish'): # definindo apenas um valor como default
    '''Exibe informações sobre um animal de  estimação.'''
    print('\nEu tenho um(a){}'.format(tipo).upper())
    print('O nome do meu {} é {}.'.format(tipo,name).title())
descricao_pet('peixe','aquaman')
descricao_pet('hamster','mouse')
descricao_pet(tipo='dog', name='cat')
descricao_pet(name='morgana')
descricao_pet(name='frank',tipo='porco')
