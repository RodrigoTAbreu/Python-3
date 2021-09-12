from datetime import date
maiores = 0
menores = 0
for c in range(1,8):
    ano = int(input('Informe o ano de nascto. da {}ª pessoa: '.format(c)))
    atual = date.today().year
    idade = atual - ano
    if idade >= 21:
        maiores +=1
    else:
        menores +=1
print('Foram inseridos {} dados.'.format(c))
print('Tivemos {} maiores.'.format(maiores))
print('Tivemos {} menores.'.format(menores))
