pizzas = ['Calabresa','Catupiry','Frango','Marguerita','Portuguesa', 'Tomate Seco']
friend_pizzas = pizzas[:]
pizzas.append('Aliche')
friend_pizzas.append('Salmão')

for pizza in pizzas:
    print('Minhas pizzas favoritas são:{}'.format(pizza))

for pizza_amigo in friend_pizzas:
    print('As pizzas favoritas do meu amigo são: {}'.format(pizza_amigo))