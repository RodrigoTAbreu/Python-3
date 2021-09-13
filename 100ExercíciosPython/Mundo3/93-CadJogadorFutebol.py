dadosJogador = {
    'NOME':str(input('Nome do Jogador: '))
}
partida = int(input('Quantas Partidas Jogou?: '))
c = 0
gol = []

if partida > 0:
    dadosJogador['Partida'] = partida

while c < partida:
    gol.append(int(input(f'Quantos gols na partida {c+1}º: ')))
    c+=1

dadosJogador['Gols'] = gol

print('**'*20)
print(dadosJogador)
print('**'*20)

for k, v in dadosJogador.items():
    print(f'O campos {k} tem valor {v}.')
print(f'O campo total tem o valor {sum(dadosJogador["Gols"])}')
print('**'*20)
print(f'O jogador {dadosJogador["NOME"]} jogou {partida} partidas.')

for k, vlr in enumerate(gol):
    print(f'   => Na partida {k+1} marcou {vlr} gols.')
print(f'Foi um total de {sum(gol)} gols.')