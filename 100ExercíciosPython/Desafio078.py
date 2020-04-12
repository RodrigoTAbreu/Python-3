lista= list()
for c in range(0,6):
    lista.append(int(input(f'Digite o valor da posição {c}: ')))
lista.sort()
maior = max(lista)
menor = min(lista)

if maior in lista:
    #print(lista.index(maior))
    print(f'Maior numero da lista {maior}')

if menor in lista:
    #print(lista.index(menor))
    print(f'Menor numero da lista {menor}')
print(lista)
print('Maior numero da lista: ', end='')
print(lista[0])
print('Menor numero da lista: ', end='')