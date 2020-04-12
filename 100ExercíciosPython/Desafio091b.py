from random import randint
from time import sleep
from operator import itemgetter # metodo importado para conseguir colocar em ordem
players = {'jogador1': randint(1,6),
           'jogador2': randint(1,6),
           'jogador3': randint(1,6)}
ranking = list()
print('Os valores sorteados são:')
for k, v in players.items():
    sleep(1)
    print(f'O {k} tirou {v} no dado.')
ranking = sorted(players.items(),key=itemgetter(1)) # aplicando itemgetter ao sorted
print(ranking)
for i in ranking:
    print(f'{i}')
