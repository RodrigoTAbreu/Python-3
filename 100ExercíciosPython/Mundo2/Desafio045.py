from random import randint
from  time import sleep
print('**'*30)
print(' '*20,'Vamos Jogar:JOKENPÔ')
print('**'*30)
print('''Suas Opções São:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opção = int(input('Qual é a sua escolha?: '))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
minha = randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('Minha Escolha foi {}'.format(itens[minha]))
if opção == minha:
    print('DEU EMPATE, Vamos Jogar novamente.')
elif opção == 0 and minha == 1:
    print('GANHEI, kkkk :-)')
elif opção == 0 and minha == 2:
    print('Você Ganhou :-( ')
elif opção == 1 and minha == 2:
    print('Ganhei, kkkk :-)')
elif opção == 1 and minha == 0:
    print('Você Ganhou :-(')
elif opção == 2 and minha == 0:
    print('GANHEI, kkkk :-)')
elif opção == 2 and minha == 1:
    print('Você Ganhou :-(')
else:
    opção >=3
    print('Opção Inválida')