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
   print('Muito Bem, agora eu vou escolher',end='')
   sleep(1)
   print('.',end='')
   sleep(1)
   print('.')
   print('=='*20)
   computador = randint(0,10)
   soma = jogador + computador
   print(f'Você escolheu {parImpar} e jogou {jogador}, o computador jogou {computador}. Total {soma}')
   print('=='*20)
   if parImpar == 'P':
      if soma % 2 == 0:
         venceu +=1
         print('Deu PAR.')
         print('Parabéns. Você venceu')
      else:
         print('Deu IMPAR.')
         print('Você perdeu.')
         break
   elif parImpar == 'I':
      if soma %2 !=0:
         print('Deu PAR.')
         print('Parabéns. Você venceu')
         venceu +=1
      else:
         print('Deu IMPAR')
         print('Você perdeu. ')
         break
print('-='*20)
print('Game Over.')
print(f'Você venceu {venceu} vez')
print('-='*20)
