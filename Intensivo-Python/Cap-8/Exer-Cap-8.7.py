def album(artista,disco,faixa=''):
    disco_um = {'Cantor':artista,'Disco':disco}
    if faixa:
        disco_um['Faixa'] = faixa
    return disco_um
nome_disco = album('Sei lá','Musica boa')
print(nome_disco)