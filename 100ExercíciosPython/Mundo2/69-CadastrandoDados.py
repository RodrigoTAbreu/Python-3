total = totalFMenor = totalMasc = 0
while True:
    print('**'*20)
    print(' '*8,end='')
    print('Cadastro de Pessoas')
    print('**'*20)
    idade =int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo[M/F]:').upper()[0]
    continua = ' '
    while continua not in 'SN':
        continua = input('Continua[S/N]:').upper()[0]
    if idade > 18:
        total += 1
    if sexo == 'M':
        totalMasc += 1
    if sexo == 'F' and idade <=20:
        totalFMenor += 1

    if continua == 'N':
        break
print('**'*20)
print(f'Total cadastrado {total} maior de 18')
print(f'Total de HOMENS: {totalMasc}')
print(f'Total de Mulheres menores de 20:{totalFMenor}')
print('**'*20)
