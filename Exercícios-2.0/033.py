n1 = int(input('Primeiro: '))
n2 = int(input('Segundo: '))
n3 = int(input('Terceiro: '))
menor = maior = 0
if n1 > n2 and n1 > n3:
    maior = n1
else:
    menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
else:
    menor = n2
if n3 > n2 and n3 > n1:
    maior = n3
else:
    menor = n3

print('O Maior é {}'.format(maior))
print('O Menor é {}'.format(menor))