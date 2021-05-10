rios = {
    'Nilo':'Egito',
    'Araguaia':'Brasil',
    'Aure':'França',
    'Danúbio': 'Alemanha',
}
for rio, local in rios.items(): #criando duas variáveis para serem percorridas RIO(chave) LOCAL(valor da chave)
    print('O {} corre pelo {}.'.format(rio, local ))
print('--'*20)
print('Rios do Dicionário: ')
for rio in rios.keys():
    print(rio)
print('--'*20)
print('Paises do Dicionário:')
for local in rios.values():
    print(local)