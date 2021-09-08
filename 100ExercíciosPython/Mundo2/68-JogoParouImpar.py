from random import randint
from time import sleep
print('**'*20)
print(8*' ',end='')
print('Jogo do Par ou Impar')
print('**'*20)
jogador= computador = venceu =soma =  0
while True:
   jogador = int(input('Digite um valor de 1 a 10: '))
   parImpar = str(input('Você quer Par ou Impar [P/I]:')).strip().upper()[0]
   print('~~'*20)
   print('Muito Bem, prepare-se',end='')
   sleep(1)
   print(' 1.',end='')
   sleep(1)
   print('2.',end='')
   sleep(1)
   print('3.')
   print('=='*30)
   computador = randint(0,10)
   soma = jogador + computador
   print(f'Você escolheu {parImpar} e jogou {jogador}, o computador jogou {computador}. Total {soma}. ',end='')
   print('DEU PAR.'if soma %2 ==0 else 'DEU IMPAR.')
   print('=='*30)
   #while parImpar not in 'PI': poderia ter usado um validador de entrada para PAR ou IMPAR
   if soma %2 == 0 and parImpar == 'P':
      venceu +=1
      print('Parabéns. Você venceu. Vamos jogar mais uma vez.')
      print('~~' * 20)
   elif soma %2 ==0 and parImpar == 'I':
      print('Você perdeu.',end='')
      break
   elif soma%2 !=0 and parImpar == 'I':
      print('Parabéns. Você venceu. Vamos jogar mais uma vez.')
      print('~~' * 20)
      venceu +=1
   elif soma%2 != 0 and parImpar == 'P':
      print('Você perdeu. ',end='')
      break
#print('-='*20)
print('Game Over!!!.')
if venceu != 0:
   print(f'Você venceu {venceu} vez.')
else:
   print('Mais sorte da próxima vez.!!!')
print('-='*20)
