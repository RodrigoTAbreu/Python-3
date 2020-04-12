dados = list()
lista = list()
resp = ' '
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    lista.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]

    if resp in 'Nn':
        break


print(f'Foram cadastradas {len(lista)} pessoas.') # com o LEN(lista) mostra o tamanho da lista.
print(f'Os maior Peso: {maior} Kg.', end='')
for p in lista:
    if p[1] == maior:
        print(f'[ {p[0]} ]', end='')
print()
print(f'Os menor Peso: {menor} Kg.',end='')
for p in lista:
    if p[1] == menor:
        print(f'[ {p[0]} ]', end='')
