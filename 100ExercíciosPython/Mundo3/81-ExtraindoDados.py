lista = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    resp = input('Quer continuar? [S/N]: ').upper()[0]

    if resp == 'N':
        break

if 5 in lista:
    print('O 5 faz parte da lista.')
else:
    print('O 5 não faz parte da lista.')

print(lista)
print(f'Foram digitados {len(lista)} numeros na lista.')
lista.sort(reverse=True)
print(f'Lista em orde decrescente {lista}.')