print('=='*25)
print('Calulando aumento de salário.')
print('=='*25)
sal = float(input('Qual é o salário? R$ '))
aumento = (sal *15) /100
salreal = sal + aumento
print(' Valor do salário é de R${:.2f} com 15% de aumento vai para R${:.2f}.'.format(sal, salreal))
