sal = float(input('Informe o salário: '))
if sal > 1250:
    aumento = (sal * 10) / 100
    print('O aumento foi de 10% R$ {:.2f}'.format(aumento+ sal))
elif sal <= 1250:
    aumento = (sal * 15) / 100
    print('O aumento foi de 15% R$ {:.2f}'.format(aumento + sal))
