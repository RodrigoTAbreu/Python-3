import random
print('Olá eu sou o Computador, vou escolher um Número de 0 a 5')
print("Pronto, já escolhi. Tente adivinhar qual numero eu escolhi.")
n = int(input('Vamos, digite agora: '))
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
lista = [n1, n2, n3, n4, n5]
escolha = random.choice(lista)
if escolha == n:
    print('Você acertou!!! eu escolhi {}'.format(escolha))
else:
    print('Você errou ...kkkkk escolheu {} e eu escolhi {}'.format(n, escolha))


