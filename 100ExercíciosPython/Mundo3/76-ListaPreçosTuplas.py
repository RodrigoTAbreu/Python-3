produtos = ('TV', 100,
            'Radio', 80,
            'Cama', 800,
            'Relogio', 500)

print('**'*30)
print(f'{"Listagem de Preço":^40}')
print('**'*30)
for pos in range(0,len(produtos)):
    if pos%2 == 0:
        print(f'{produtos[pos]:.<30}',end='')
    else:
        print(f'R$ {produtos[pos]:>5.1f}')
print('**'*30)