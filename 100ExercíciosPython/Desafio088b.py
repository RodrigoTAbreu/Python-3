from time import sleep
from random import randint
jogo = []
jogos = []
cont = 0
print('--'*30)
print('  '*10, 'JOGO DA MEGA SENA')
print('--'*30)
print()
resp = int(input(('Quantos jogos você quer gerar ?:')))
print()
tot = 1
while tot <= resp:
    cont = 0
    while True:
        aposta = randint(1,60)
        if aposta not in jogo:
            jogo.append(aposta)
            cont +=1
        if cont >=6:
            break
    jogo.sort()
    jogos.append(jogo[:])
        #print(f'JOGO {cont} = {jogo}')

    jogo.clear()
    tot+=1

print('-='*5,f'SORTEANDO {resp}','-='*5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print()
print('<'*10, end='')
print('Fim das Apostas', end='')
print('>'*10)