def area(l, c):
    total = l * c
    print(f'A área total do terreno com Largura {l} x {c} é de {total}mts')
    print('--'*30)

print('Controle de Terrenos')
print('--'*30)
area(l=float(input('LARGURA(m): ')), c=float(input('COMPRIMENTO(m): ')))
