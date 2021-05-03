import random
import emoji
escolhe = int(input('Escolha um número: '))
numeros = random.randrange(0,10)

if escolhe == numeros:
    print(emoji.emojize('Parabéns, você acertou.:thumbs_up:',use_aliases=False))
else:
    print(emoji.emojize('Você errou. Tente novamente.:thumbs_down:',use_aliases=False))

print('Computador escolheu {} \ne você escolheu {}'.format(numeros, escolhe))