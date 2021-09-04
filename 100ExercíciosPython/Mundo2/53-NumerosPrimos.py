n = int(input('Informe um número: '))
cont = 0
#IDENTIFICANDO SE O RESTO DA DIVISÃO É ZERO OU NÃO
for c in range(1,n + 1):
    if n %c == 0:
        cont += 1
        print('\033[34m',end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c),end=' ')

print('\n \033[m O nº {} foi divisível por {} vezes.'.format(n,cont))
#IDENTIFICANDO SE O NÚMERO É PRIMO
if cont == 2:
    print('O número {} é PRIMO !!'.format(n))
else:
    print('O número NÃO é PRIMO')