dados = dict()
gols = list()
dados['Nome'] = str(input('Nome do Jogador: ')).upper()
qtd = int(input(f'Quantas Partidas {dados["Nome"]} jogou ?: '))
for g in range(0,qtd):
    gols.append(int(input(f'Quantos Gols na partida {g}:')))
    dados['Gols'] = gols
    dados['Total'] = sum(gols)
print('-='* 30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O Campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador \033[4m{dados["Nome"]}\033[m jogou \033[4m{qtd}\033[m partidas.')
for i, g in enumerate(gols):
    print(f'-->> Na partida {i}, fez {g} gols')

print(f'Foi um total de {dados["Total"]} Gols.')
print('-='* 30)
print('fim')