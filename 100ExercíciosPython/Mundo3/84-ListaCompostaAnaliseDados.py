dados = []
lista = []
maior = 0
menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))

    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    lista.append(dados[:])
    dados.clear()

    resp = input('Deseja continuar? [S/N]: ').upper()[0]
    if resp == 'N':
        break

print(f'Foram cadastrados ao total {len(lista)} pessoas.')
print(f'A pessoa mais pesada tem {maior}Kg.')

for pessoa in lista:
    if pessoa[1] == maior:
        print(f' [{pessoa[0]}] é a pessoa mais pesada.')
print()

print(f'A mais leve tem {menor}kg')
for pessoa in lista:
    if pessoa[1] == menor:
        print(f'Pessoa [{pessoa[0]}] é a mais leve.')
