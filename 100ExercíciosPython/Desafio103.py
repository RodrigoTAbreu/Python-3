def ficha(nome, gol):
        
    if nome == '':
        print(f'O Jogador <desconhecido> fez {gol}')
    elif gol == '':
        print(f'O jogador {nome} fez 0 gol')
    elif nome == gol == '':
        print('O jogador <desconhecido> marcou 0 gols')


nome = str(input('Nome do Jogador: '))
gol = str(input('Número de Gols: '))
ficha(nome,gol)