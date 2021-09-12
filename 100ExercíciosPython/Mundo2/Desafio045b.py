from random import randint
from time import sleep
print('**'*30)
print(' '*20,'Vamos Jogar:JOKENPÔ')
print('**'*30)
print('''Suas Opções São:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('-='*20)
jogador = int(input('Escolha uma Opção: '))

if jogador != 0 and jogador != 1 and jogador !=2:
    print('Opção \033[1;30;43mInválida\033[m \n Jogue novamente.')
else:
    print('Computador Escolheu {}'.format(itens[computador]))
    print('Jogador Escolheu {}'.format(itens[jogador]))

    sleep(1)
    print('-='*20)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ !!!!')

if computador == 0: #computador escolhe pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1: #jogador escolhe papel
        print('Parabéns!! \033[1;31;47mVocê Ganhou\033[m')
    elif jogador == 2: #jogador escolhe tesoura
        print('Computador \033[1;33;47mGanhou\033[m')

elif computador == 1: #computador escolhe papel
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2: #jogador escolhe tesoura
        print('Parabéns \033[1;33;47mVocê Ganhou\033[m')
    elif jogador == 0: #jogador escolhe pedra
        print('Computador \033[1;31;47mGanhou\033[m')

elif computador == 2: #computador escolhe tesoura
    if jogador == 2:
        print('EMPATE')
    elif jogador == 0: #jogador escolhe pedra
        print('Parabéns \033[1;33;47mVocê Ganhou\033[m')
    elif jogador == 1: #jogador escolhe papel
        print('Computador \033[1;31;47mGanhou\033[m')

