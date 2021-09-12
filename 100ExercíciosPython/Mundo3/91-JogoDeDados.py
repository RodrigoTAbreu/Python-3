from random import randint
from operator import itemgetter
resultados = {
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)}
ranking = dict()
print('=='*30)
print('Valores sorteados.')
print('=='*30)
for k, v in resultados.items():
    print(f'O {k} tirou {v} no dado.')
ranking = sorted(resultados.items(),key=itemgetter(1), reverse=True)
print('=='*30)
print('Ranking dos Jogadores')
print('=='*30)
for i, v in enumerate(ranking):
    print(f'O {i+1}° lugar:{v[0]} com {v[1]} pontos')

