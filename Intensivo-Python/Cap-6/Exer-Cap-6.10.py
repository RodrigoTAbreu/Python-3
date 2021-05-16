numeros = {
    'Maria':[5,6,7],
    'joão':[8,9,7],
    'Pedro':[4,5,6],
    'ana':[3,2,5]
}
for dado, numero in numeros.items():
    print('O(a) Cliente {}'.format(dado))
    for escolha in numero:
        print('\t escolheu a opção: {}'.format(escolha))