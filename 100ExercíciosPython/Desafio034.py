sal = float(input('Qual o salário do Funcionário? R$'))
if sal > 1500:
    aumento = (sal * 10 / 100) + sal
    print('O salário do funcionário passará a ser de R${}'.format(aumento))
else:
    aumento = (sal * 15 / 100) + sal
    print('O salário do funcionário passará a ser de R${}'.format(aumento))