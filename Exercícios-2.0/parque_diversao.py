idade_pessoas = int(input('Bem vindo ao Parque. Qual é a idade ? '))
if idade_pessoas <= 4:
    preço = 0
elif idade_pessoas <=18:
    preço = 10
elif idade_pessoas < 65:
    preço = 20
else:
    preço = 25
print('\nOlá seja bem vindo ao Parque')
print('Seu ingresso curstará R${}'.format(preço))
print('Boa Diversão!!')



