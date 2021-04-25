print('=='*25)
print('Calulando Desconto de um Produto.')
print('=='*25)
prod = float(input('Valor do Produto:R$ '))
desc = prod * 5/100
vreal = prod - desc
# ou podemos fazer da seguinte forma
# desc = prod - (prod * 5 /100)
print('O Valor do produto é R$ {:.2f} com desconto de 5% vai para R$ {:.2f}'.format(prod, vreal))
print('Você conseguiu economizar R${:.2f} em desconto.'.format(desc))