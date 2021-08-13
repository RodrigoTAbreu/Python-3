nome = str(input('Qual é seu nome: '))
if nome == 'Rodrigo':
    print('Nome legal !!')
elif nome=='Pedro' or nome == 'Maria' or nome =='José':
    print('Esse é um nome Bíblico.')
elif nome in 'Ana Claudia Beatriz':
    print('Bom dia Linda !!!')
else:
    print('Mais um nome comum.')
print('Tenha um bom dia, {}!'.format(nome))
