from random import randint
print('-='*10,end='')
print(' Jogo da Adivinhação ',end='')
print('=-'*10)
print('Vamos, jogar. Eu escolhi um número de 0 até 10. Qual é?')
computador = randint(0,10) #computador vai escolher um número de 0 a 10
#print(computador)
player = int(input('Digite seu palpite: ')) #jogador digita um número
#print(player)
cont = 0 # contador dos palpites ou chances
acertou = False #variavel que é false até que ele acerte e mude para TRUE
while not acertou: # enquanto não acertou
    cont += 1 #contagem dos palpites se inicia
    if cont == 1:
        print('Tá dificil ??!!! Vou te ajudar. ')
    player = int(input('Digite um número para adivinhar: ')) #jogo solicita a entrada de mais uma tentativa.
    if player == computador: #se o jogador digitar um número igual ao do computador
        acertou = True # muda a variável para TRUE
    else:        # se for diferente o jogo vai dar algumas dicas
        if player > computador: #se o jogador escolher um numero maior que o do computador
            print('Menos..')
        elif player < computador: #se o jogador escolher um numero menor que o do computador
            print(('Mais..'))
print('Você acertou com {} tentativas. Parabéns!!'.format(cont))
