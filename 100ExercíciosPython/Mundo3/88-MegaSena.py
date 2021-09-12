from time import sleep
from random import randint
jogo = [] # define a lista
cont = 0 #inicia o contador em 0
print('--'*30)
print('  '*10, 'JOGO DA MEGA SENA')
print('--'*30)
resp = int(input(('Quantos jogos você quer gerar ?:')))# entrada dos números.
print('-='*10, end='')
print(f' SORTEANDO {resp} JOGOS ', end='')
print('-='*10)
while cont < resp:#enquanto o CONT menor que RESP
    for numero in range(1,7): #para numero in range de 1 a 7
        aposta = randint(0,60) #variavel APOSTA recebe um numero aleatprio de 0 a 60
        if aposta not in jogo: #se a variavel APOSTA não estiver na lista JOGO
            jogo.append(aposta) # ele adiciona o valor na lista
    cont +=1 # soma mais 1 ao contador
    jogo.sort() # coloca a lista em ordem
    print(f'JOGO {cont} = {jogo}') #imprime o contador e a lista com os jogos.
    sleep(0.5) # tempo de espera
    jogo.clear() # limpa a lista
print('=-'*10, end='')
print('Fim das Apostas', end='')
print('-='*10)
