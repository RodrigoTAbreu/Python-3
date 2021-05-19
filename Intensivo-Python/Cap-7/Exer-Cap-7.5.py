msg = 'Bem Vindo ao nosso Cinema.'

total = 0
while True:
    print(msg)
    idade = int(input('\nInforme a Idade de cada um. [00] Para finalizar: '))
    if idade == 00:
        break
    if idade <= 3:
        print('Essa pessoa não paga.')
    elif idade <= 12:
        total = total + 10
        print('Essa pessoa paga R$10,00')
    elif idade >=13:
        total = total +  15
        print('Essa pessoa paga R$15,00')

print('Total a pagar é R${},00.'.format(total))