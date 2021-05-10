#Armazena as informações sobre uma pizza que está sendo pedida
pizza = {
    'massa':'grossa',
    'borda':['cheddar','catupyri'],

}
#Resumo do pedido
print('Você pediu {} - massa da pizza, com a borda'.format(pizza['massa']))

for bordas in pizza['borda']:
    print('\t{}'.format(bordas))