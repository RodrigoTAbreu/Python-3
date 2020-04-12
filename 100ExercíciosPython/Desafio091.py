from random import randint
from time import sleep

players = {}
players['jogador1'] = randint(1,6)
players['jogador2'] = randint(1,6)
players['jogador3'] = randint(1,6)
print('Os valores sorteados são: ')
for k, v in players.items():
    sleep(1)
    print(f'O {k} tirou {v}')
print('O Ranking dos jogadores é: ')
sleep(1)
for k,v in players.items():
    print(sorted(players[k]))
    #print(f'{k}',sorted(players.values()))
