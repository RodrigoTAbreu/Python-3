n = int(input('Qual é o primeiro Termo: '))
r = int(input('Qual é a razão: '))
decimo = n + (10-1)*r
cont = 0
for c in range(n,decimo + r,r):
    cont +=1
    print('->{}..{}'.format(cont, c),end=' ')
print('acabou')