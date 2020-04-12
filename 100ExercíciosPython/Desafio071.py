print('+'*30)
un = de = ce = n20 = int
nota50 = 50
while True:
    saque = int(input('Informe o Valor do Saque: R$'))
    un = saque // 1 % 10
    de = saque // 10 % 10
    ce = saque // 100 % 10

    if ce != 0:
        nota50 = saque / 50
        print('Total de {:.0f} cédulas de R$ 50,00'.format(nota50))
    if de !=0:
        if de % 2 == 0:
            n20 = de // 1 % 10
            print('Total de {:.0f} cédulas de R$ 20,00'.format(de))
        else:
            print('Total de {:.0f} cédulas de R$ 10,00'.format(de))
    if un != 0:
        print('Total de {:.0f} cédulas de R$ 1,00'.format(un))
    print('Volte Sempre')
    break










