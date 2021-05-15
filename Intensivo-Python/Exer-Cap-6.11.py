cidades = {
    'SP':{
        'country':'Brasil',
        'population':'1Milhao',
        'fact':'Capital das Finanças'
    },
    'Viena':{
        'country': 'França',
        'population': '200Mil',
        'fact': 'Cidade Linda'
    },
    'New_york':{
        'country': 'EUA',
        'population': '2Milhoes',
        'fact': 'Capital do Mundo'
    }
}

for cidade, pais in cidades.items():
    print('Nome da cidade:{}\n\tPais:{}\n\tPopulação:{}.\n\tFato:{}'.format(cidade,pais['country'],pais['population'],pais['fact']))
    #for local in pais:

     #  print('{}-->>'.format(local('country')))