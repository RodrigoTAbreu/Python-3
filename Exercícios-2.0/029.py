import emoji
velo = int(input('Qual a velocidade? '))

if velo > 80:
    multa = 7
    valor_multa = (velo-80)*7
    print(emoji.emojize('Você foi multado.:police_car:',use_aliases=True))
    print('Você foi multado em R${}.'.format(valor_multa))

else:
    print(emoji.emojize('Dirija com cuidado.:checkered_flag:',use_aliases=True))
