def ficha(nome = '',gols =' '):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if nome == '':
        print(f'Nome do jogador não foi especificado, e marcou {gols} gols.')
    elif gols == 0:
        print(f'O Jogador {nome} não marcou gols. ')
    elif nome == '' and gols == '':
        print('Nenhum dado foi especificado.')
    else:
        print(f'O Jogador {nome} marcou {gols} gols. ')


ficha(str(input('Nome do Jogador:')),str(input('Qtd de Gols:')))