import random
import time
import emoji

print('----JO¬¬KEN¬¬PO ----')
opcao = int(input('''Escolha sua opção:
                  [0] - Papel
                  [1] - Pedra
                  [2] - Tesoura
                  '''))
computador = random.randint(0,2)
item = ['PAPEL', 'PEDRA', 'TESOURA']

print('Muito bem. Eu já escolhi a minha opção. Vamos Jogar !!\n')
time.sleep(1)
print('--JO--')
time.sleep(1)
print('--KEN--')
time.sleep(1)
print('--PÔ--')
print('Você escolheu a opção {}'.format(item[opcao]))
print('Eu escolhi {}'.format(item[computador]))

if computador == opcao:
    print('Deu empate, vamos jogar novamente.')
    print( emoji.emojize( ":anguished:", language="en", use_aliases=True ) )
elif opcao == 0 and computador == 2 :
    print('Computador GANHOU !!!! Você PERDEU ....kkkkk')
    print(emoji.emojize( ":1st_place_medal:", language="en", use_aliases=True ))
elif opcao == 1 and computador == 2:
    print('Você ganhou. PARABÉNS !!!')
    print( emoji.emojize( ":1st_place_medal:", language="en", use_aliases=True ) )
elif opcao == 0 and computador == 1:
    print( 'Você ganhou. PARABÉNS !!!' )
    print(emoji.emojize( ":1st_place_medal:", language="en", use_aliases=True ))
elif opcao == 2 and computador == 0:
    print( 'Você ganhou. PARABÉNS !!!' )
    print(emoji.emojize( ":1st_place_medal:", language="en", use_aliases=True ))
elif computador == 0 and opcao == 1:
    print( 'Computador GANHOU !!!! Você PERDEU ....kkkkk' )
    print(emoji.emojize( ":1st_place_medal:", language="en", use_aliases=True ))
elif computador == 1 and opcao == 2:
    print( 'Computador GANHOU !!!! Você PERDEU ....kkkkk' )
    print(emoji.emojize( ":1st_place_medal:", language="en", use_aliases=True ))
