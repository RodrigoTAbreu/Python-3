n1 = (int(input('Digite o primeiro: ')),
        int(input('Digite segundo: ')),
        int(input('Digite o terceiro: ')),
        int(input('Digite o quarto: ')))

if 9 in n1:
    print(f'O Valor 9 apareceu {n1.count(9) } vez')
else:
    print('9 não foi inserido.')
if 3 in n1:
    print(f'O numero 3 apareceu na posição {n1.index(3,0)}')
else:
    print('3 não foi digitado')
print('Os valores pares encontrados foram, ', end='')
for n in n1:
    if n %2 == 0:
        print(f'{n},', end=' ')