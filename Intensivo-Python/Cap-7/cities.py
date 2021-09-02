m = 'Digite o nome da Cidade.'
m += '\nDigite QUIT para sair.'
cidades = []

while True:
    city = input(m)
    if city == 'quit':
        break
    else:
        cidades.append(city)
        print('Você adicionou {} a lista'.format(city))

print('As cidades listadas são: {}'.format(cidades))