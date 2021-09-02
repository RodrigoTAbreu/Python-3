def album(artista,disco, faixa=''):
    disco = {'artista':artista,'Disco':disco,'Faixa':faixa}
    return disco

while True:
    print('\nInforme os dados. Pressione [q] para finalizar.')
    nome_artista = input('Nome do artista: ')
    if nome_artista == 'q':
        break
    nome_disco = input('Nome do disco: ')
    if nome_disco == 'q':
        break
    faixa_disco = input('Informe a faixa: ')
    if faixa_disco == 'q':
        break
    dados = album(nome_artista,nome_disco,faixa_disco)
    print('O artista é{}'.format(dados))