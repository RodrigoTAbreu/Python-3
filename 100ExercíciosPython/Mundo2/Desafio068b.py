from random import choice
from random import randint
result= 0
vitoria = 0
while True:
    n = int(input('Informe um Numero: '))
    comp = randint(0, 10)
    result = n + comp
    tipo = ' '


    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print( f'Você Digitou {n} e O computador escolheu o numero {comp}, total foi {result}' )
    print( 'DEU PAR' if result % 2 == 0 else 'DEU IMPAR' )
    if tipo == 'P':
        if result % 2 == 0 :
            print("Voce Ganhou !")
            vitoria += 1
        else:
            print('Você Perdeu')
            break
    if tipo == 'I':
        if result % 2 !=0:
            print('você Ganhou')
            vitoria += 1
        else:
            print('Voce Perdeu')
            break

    print('Vamos Jogar Novamente!!!')
print(f'Você venceu {vitoria} vezes')

