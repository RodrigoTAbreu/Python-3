a = int(input('Primeiro: '))
b = int(input('Segundo: '))
c = int(input('Terceiro: '))
#verificando o menor valor
menor = a
if b < c and b < a:
    menor = b
if c<a and c<b:
    menor = c
print('O Menor é {}'.format(menor))
# verificando o maior
maior = a
if b >c and b > a:
    maior = b
if c > a and c > b:
    maior = c

print('O Maior é {}'.format(maior))
print('A soma de ambos é {}'.format(menor+maior))
