from random import randint
from time import sleep
print('-='*20)
print('         JOGO- JO KEN PO')
print(('=-'*20))
jogador = int(input('''
Escolha uma das Opções:
[1] - PEDRA
[2] - PAPEL
[3] - TESOURA
Sua Escolha: '''))
computador = randint(1,3)
sleep(1)
print(' JO ')
sleep(1)
print(' KEN ')
sleep(1)
print(' PO ')

if jogador == 1 and computador == 3:
    print('Você escolheu PEDRA e eu escolhi TESOURA. Você Ganhou !!! Parabéns.')
elif jogador == 1 and computador == 2:
    print('Você escolheu PEDRA e eu escolhi PAPEL Você Ganhou !!! Parabéns.')
    print('Computador Ganhou. Parabéns para mim !!!')
elif jogador == 2 and computador == 1:
    print('Você escolheu PAPEL e eu escolhi PEDRA. Você Ganhou !!! Parabéns.')
elif jogador == 2 and computador == 3:
    print('Você escolheu PAPEL e eu escolhi TESOURA. Você Ganhou !!! Parabéns.')
    print('Computador Ganhou. Parabéns para mim !!!')
elif jogador == 3 and computador == 2:
    print('Você escolheu TESOURA e eu escolhi PAPEL. Você Ganhou !!! Parabéns.')
elif jogador == 3 and computador == 1:
    print('Você escolheu TESOURA e eu escolhi PEDRA. Você Ganhou !!! Parabéns.')
    print('Computador Ganhou. Parabéns para mim !!!')
else:
    print('EMPATE. Jogue novamente.')


print('Sua esolha {}'.format(jogador))
print('Computador escolheu {}'.format(computador))
