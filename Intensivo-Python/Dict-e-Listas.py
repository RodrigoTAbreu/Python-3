#armazena informações sobre uma pizza que está sendo pedida
pizza = {
    'massa' : 'grossa',
    'ingredientes': ['tomates','queijo-extra']
}

#Resume o pedido

print('Você pediu {}'.format(pizza['massa']))

for ingrediente in pizza['ingredientes']:
    print('\t{}'.format(ingrediente))
#para cada ingrediente IN dicionario PIZZA na posição 'INGREDIENTES'
