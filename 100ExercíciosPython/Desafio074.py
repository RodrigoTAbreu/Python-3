from random import randint
n = (randint(1,10), randint(1,10), randint(1,10),
     randint(1,10), randint(1,10))
print('Numeros sorteados: ', end='')
for c in n:
    print(f'{c} ', end='')
print(f'\nMaior numero foi: {max(n)}')
print(f'Menor numero foi: {min(n)}')