vlr = 0
cont = 0
for c in range(1, 501,2 ):
    if c % 3 == 0:
        vlr = vlr + c
        cont= cont+1
        #print(c, end=' ')
print('\n',vlr)
print('Total de números {}'.format(cont))

print('Fim!!')