time = list()
dados = dict()
gols = list()
while True:
    dados.clear()
    dados['Nome'] = str(input('Nome do Jogador: ')).upper()
    qtd = int(input(f'Quantas Partidas {dados["Nome"]} jogou ?: '))
    gols.clear()
    for g in range(0,qtd):
        gols.append(int(input(f'Quantos Gols na partida {g}:')))
    dados['Gols'] = gols[:]
    dados['Total'] = sum(gols)
    time.append(dados.copy())
    while True:
        resp = str(input('Deseja Continuar?: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO!! Digite S ou N')
    if resp == 'N':
        break
print('-'*40)
print('Cod.', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    op = int(input('Digite o Cod. do Jogador para ver detalhes.[999-sair]:'))
    if op == 999:
        print('Finalizando programa...')
        break
    if op >= len(time):
        print('Erro! Digite o código válido')
    else:
        print(f'Levantamento do Jogador {time[op]["Nome"]}')#OP é o indice que está dentro da lista time e "NOME" está dentro do dicionario.
        for i,g in enumerate(time[op]["Gols"]):
            print(f' No jogo {i+1} fez {g} gols.')
    print('-'*40)
print()

