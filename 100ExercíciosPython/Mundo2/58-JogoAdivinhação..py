from random import randint
print('-='*10,end='')
print(' Jogo da Adivinhação ',end='')
print('=-'*10)
print('Vamos, jogar. Eu escolhi um número de 0 até 10. Qual é?')
computador = randint(0,10)
#print(computador)
player = int(input('Digite seu palpite: '))
#print(player)
cont = 0

while player != computador:
    cont += 1
    print('Você errou tente novamente.')
    player = int(input('Digite um número para adivinhar: '))

    if player > computador:
        print('Menos..')
    elif player < computador:
        print(('Mais..'))
print('Você acertou com {} tentativas. Parabéns!!'.format(cont))
