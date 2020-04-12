media = float(0)
pessoa = 0
anos = 0
idadehvelho = 0
nomehvelho = 0
idade = 0
mulher = 0
nome = 0
for d in range(1,5):
    nome = input('Nome da pessoa:')
    idade = int(input('Idade da pessoa: '))
    sexo = input('Sexo [M/F]:')
    pessoa +=1
    anos += idade
    if sexo = M:
        idadehvelho = idade
        nomehvelho = nome
    if sexo = F:
        if idade <20:
            mulher +=1

media = anos / pessoa
print('A media de idade do grupo é {}.'.format(media))
print('O nome do Homem mais velho {}'.format(nomehvelho))
print('Temos {} mulheres abaixo dos 20 anos'.format(mulher))