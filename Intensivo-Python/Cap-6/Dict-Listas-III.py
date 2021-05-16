linguagens_favoritas = {
    'João': ['python','ruby'],
    'Sara': ['c'],
    'Eduardo': ['ruby','go'],
    'Kelly':['JavaScript'],
    'Phil': ['python','haskell'],

}

for nome, linguagens in linguagens_favoritas.items():
    if len(linguagens) == 1:
        print('{} tem apenas a linguagem {} como favorita'.format(nome, linguagens))
    else:
        print('{} e linguagem é :'.format(nome))
        for linguagen in linguagens:
            print('\t{}'.format(linguagen))