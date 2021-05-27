def make_pizza(size, *toppings):
    '''Apresenta a pizza que estamos prestes a preparar'''
    print('\nPreparando a pizza de tamanho {} com os seguintes ingredientes:'.format(size))
    for topping in toppings:
        print('- {}'.format(topping))

make_pizza('Gigante','peperoni')
make_pizza('Média','queijo extra','borda de chedder','tomate seco')
