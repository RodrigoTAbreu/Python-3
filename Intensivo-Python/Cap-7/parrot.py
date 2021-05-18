m = 'diga alguma coisa e eu repetirei para você'
m += '\nDigite QUIT para sair.'

msg = ''
'''while msg !='quit':
    msg = input(m)
    if msg != 'quit': # se msg for igual ele finaliza sem imprimir nada
        print(msg)'''
active = True
while active:
    msg = input(m)
    if msg == 'quit':
        active = False
    else:
        print(msg)