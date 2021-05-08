itens_disponiveis = ['tomate seco','catupiry','cheder',
                     'palmito','aliche','batata']
itens_pedido = ['aliche', 'laranja','tomate seco']
for itens_pedido in itens_pedido:
    if itens_pedido in itens_disponiveis:
        print('Adicionado {} à pizza.'.format(itens_pedido))
    else:
        print('Desculpe, não temos {} disponível agora.'.format(itens_pedido))
print('\nPedido Finalizado.')