dados = dict()
gols = list()
jogador = list()
while True:
    #dados['Nome'] = str(input('Nome do Jogador: '))
    #jogador.clear()
    print('--'*20)
    #jogador.append(str(input( 'Nome do Jogador: ') ))
    jogador = str(input('Nome do Jogador: '))
    qtd = int(input(f'Quantas partidas {jogador[0]} jogou?'))
    for g in range(0,qtd):
        gols.append(int(input(f'Quantos gols na partida {g}: ')))
    dados['Nome'] = jogador
    dados['gol'] = gols
    while True:
        resp = str( input( 'Deseja Continuar?[S/N]: ' ) ).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO !! Digite S ou N.')
    if resp == 'N':
        break
print(dados)