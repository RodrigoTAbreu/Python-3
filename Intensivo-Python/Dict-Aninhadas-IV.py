linguagens = {'jean':['C#','Python'],
              'Roberto':['Ruby','Java'],
              'Carla':['HTML'],
              'Ana':['C#'],
              'Rodrigo':['Haskell','go'],
              'Carlinha':['JS','Python']
    }
for nome, linguagen in linguagens.items():
    if len(linguagen)>1:
        print('Tem mais de uma linguagem')
    else:
        print('apenas uma')
    '''
    for nome, linguagen in linguagens.items():
        if len(linguagen)>1:
            print('\n{}, suas linguagens favoritas são:'.format(nome.title()))
        for language in linguagen:
            print('\t{}'.format(language.title()))'''
