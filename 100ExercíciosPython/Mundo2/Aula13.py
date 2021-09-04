result = 0
for c in range(0,3):
    n = int(input('Informe o valor: '))
    #print('Contando {}'.format(c))
    c = c+1
    result = result + n
    if c == 5:
        print('Chegamos na metade da contagem.')
        print('Continuando a contagem')
print('Acabou')
print(result)

