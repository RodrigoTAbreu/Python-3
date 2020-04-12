pessoas = dict()
dados = list()
mulheres = list()
mediaacima = list()
nome = sexo = str
resp =' '
tidade = media = idade = cont = 0
while resp not in 'N':
    nome = str(input('Nome: ')).upper()
    pessoas['nome'] = nome
    idade = int(input('Idade: '))
    tidade += idade
    pessoas['idade'] = idade
    sexo = str(input('Sexo[F/M]: ')).upper().strip()[0]
    pessoas['sexo'] = sexo
    cont+=1
    media = tidade / cont
    if sexo == 'F':
        mulheres.append(nome)
    if idade > media:
        mediaacima.append(nome)
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar ?[S/N]: ')).upper().strip()[0]
        if resp != 'SN':
            print('ERRO! Digite [S] para sim ou [N] para não:')
        if resp == 'Nn':
            break
        dados.append(pessoas.copy())
print('**'*30)
print(f'Foram cadastradas {len(dados)} pessoas.')
print()
print(f'A média de idade do grupo é: {media}')
print()
print(f'As Mulheres do grupo são: {mulheres}')
print()
print(f'As pessoas com idade acima da media são: {mediaacima}')
