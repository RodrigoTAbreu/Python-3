galera = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).upper()
    while True:
        pessoas['sexo'] = str(input('Sexo: ')).upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Digite M ou F')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Deseja continuar ?: ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO!!!Digite S ou N.')
    if resp == 'N':
        break
print('**'*30) #até essa linha foi apenas leitura de dados.
print(f' A) Total de pessoas cadastradas {len(galera)}')
media = soma / len(galera)
print(f' B) A média de idade do grupo é de {media:5.2f} anos.')
print(f' C) As mulheres cadastradas foram ', end='')
for individuo in galera:
    if individuo['sexo'] in 'Ff':
        print(f'{individuo["nome"]} ', end='')
print()
print(' D) Pessoas acima da Média: ')
for individuo in galera:
    if individuo['idade'] >= media:
        print('    ', end=' ')
        for k, v in individuo.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<<fim >>>')