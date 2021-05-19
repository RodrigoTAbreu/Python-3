msg = 'O que você quer em seu AÇAI.'
msg += '\nPara finalizar digite [quit]: '
ingredientes = []

while True:
    ingre = input(msg)
    if ingre == 'quit':
        break
    else:
        ingredientes.append(ingre)
        print('Você adicionou {} ao AÇAI.'.format(ingre))
print('Muito bem. Esses são os adicionais do açai.')
print('\n{}.'.format(ingredientes))