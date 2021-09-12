lista = [[],[]] # cria a lista com as posição específica.
n = 0

for c in range(1,8):
    n = int(input(f'Digite o {c}° um número: '))
    if n %2 == 0:
        lista[0].append(n) #adicionando na posição 0
    else:
        lista[1].append(n) #adicionando na posição 1

lista[0].sort() # coloca em ordem os itens da posição 0
lista[1].sort() # coloca em ordem os itens da posição 1
print(f'Os pares são {lista[0]}.')
print(f'Os ímpares são {lista[1]}.')