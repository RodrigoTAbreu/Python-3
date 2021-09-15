def contador(i,f,p):
    c = 0
    print('=='*10)
    print('Contagem de números.')
    print('==' * 10)
    print(f'Valor de Início: {i}')
    print(f'Valor de Fim: {f}')
    print(f'Valor de Passo: {p}')
    print('**' * 10)
    for cont in range(i,f,p):
        print(f'> {cont}.',end=' ')
        c +=1


contador(int(input('Valor Inicial:')),int(input('Valor Final: ')),int(input('Passo: ')))