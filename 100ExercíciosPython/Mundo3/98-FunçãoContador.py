from time import sleep
def contador(i,f,p):
    c = r = 0
    print('=='*10)
    print('Contagem de números.')
    print('==' * 10)
    print(f'Valor de Início: {i}')
    print(f'Valor de Fim: {f}')
    print(f'Valor de Passo: {p}')
    print('**' * 10)
    if i>f:
        while i > f:
            #print(i)
            sleep(1)
            print(f'> {i}.', end=' ')
            r = i-p
            i = r
    elif i < f:
        for cont in range(i,f,p):
            sleep(1)
            print(f'> {cont}.',end=' ')
            c +=1


contador(int(input('Valor Inicial:')),int(input('Valor Final: ')),int(input('Passo: ')))