from time import sleep
from random import randint
jogo = []
cont = 0
print('--'*30)
print('  '*10, 'JOGO DA MEGA SENA')
print('--'*30)
resp = int(input(('Quantos jogos você quer gerar ?:')))
print('-='*10, end='')
print(f' SORTEANDO {resp} JOGOS ', end='')
print('-='*10)
while cont < resp:
    for numero in range(1,7):
        aposta = randint(0,60)
        if aposta not in jogo:
            jogo.append(aposta)
    cont +=1
    jogo.sort()
    print(f'JOGO {cont} = {jogo}')
    sleep(1)
    jogo.clear()
print('=-'*10, end='')
print('Fim das Apostas', end='')
print('-='*10)