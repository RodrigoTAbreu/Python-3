from time import sleep
vlr1 = int(input('Informe o primeiro valor: '))
vlr2 = int(input('Informe o segundo valor: '))
escolha = 0
resultado = 0
print('=='*30)
while not escolha == 5:
    print('Escolha uma Opção:')
    escolha = int(input('''
    [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - MAIOR
    [4] - NOVOS NÚMEROS
    [5] - SAIR
    Digite uma das opções: '''))
    print('~'*30)
    if escolha == 1:
        resultado = vlr1 + vlr2
        print('O Resultado da Soma de {}+{}={} '.format(vlr1,vlr2,resultado))
        print('~' * 30)
    if escolha == 2:
        resultado = vlr1 * vlr2
        print('O Resultado da multiplicação de {}X{}={}'.format(vlr1,vlr2,resultado))
        print('~' * 30)
    if escolha == 3:
        if vlr1 > vlr2:
            print('O primeiro valor {} é o maior'.format(vlr1))
            print('~' * 30)
        elif vlr1 < vlr2:
            print('O segundo valor {} é o maior'.format(vlr2))
            print('~' * 30)
        else:
            print('Os valores são iguais.')
            print('~' * 30)
    if escolha == 4:
        print('Informe os números novamente.')
        vlr1 = int(input('Informe o primeiro valor novo: '))
        vlr2 = int(input('Informe o segundo valor novo: '))
        print('~' * 30)
    if escolha >5:
        print('Opção inválida. Digite uma opção válida.')
        print('~' * 30)

print('Saindo do Programa.',end='')

sleep(1)
print('.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.')
print('~' * 30)
print('Fim !!!Obrigado.')

