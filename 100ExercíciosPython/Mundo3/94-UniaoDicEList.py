resp = ' '
pessoas = dict()
galera = list()
while True:
    pessoas['nome'] = str(input('Digite o nome:'))
    pessoas['sexo'] = str(input('Digite o Sexo [F/M]: '))
    pessoas['Idade'] = int(input('Qual a idade?: '))
    #galera.append(pessoas)
    galera.copy(pessoas)
    resp = str(input('Quer continuar ?[S/N]: ')).strip().upper()[0]

    if resp == 'N':
        break
    print( f'Dados da lista GALERA {galera}' )
    print( f'Dados do dicionario pessoas{pessoas}' )
    pessoas.clear()