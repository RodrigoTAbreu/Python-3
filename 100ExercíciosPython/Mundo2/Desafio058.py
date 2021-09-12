from random import randint
from time import sleep
sleep(1)
print('Jogue comigo, vou escolher um numero de 0 a 4.', end='')
print('Vou pensar..', end='')
sleep(2)
print('Aguarde...', end='')
sleep(2)
print('Pronto...escolhi. ')
print('Vamos, em que número eu pensei de 0 a 4.')
lista = randint(0,10)
jogador = int(input('Digite o seu palpite: '))
tentativas = 1

while jogador != lista:
    tentativas += 1
    jogador = int(input('Você errou, tente novamente: '))
    if jogador < lista:
        print('Vou dar uma dica. É um número MAIOR que esse.')
    elif jogador > lista:
        print( 'Vou dar uma dica. É um número MENOR que esse.' )
print('Parabéns, você digitou {} e eu escolhi {}, você precisou de {} tentativas.'.format(jogador, lista, tentativas))
