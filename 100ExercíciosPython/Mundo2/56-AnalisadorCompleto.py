nomehomem = ''
media = 0
idadeHomem = 0
idadeGrupo = []
contIdadeMulher = 0
for pessoa in range(1,5):
    print('-'*5+f' {pessoa}ª pessoa '+'-'*5)
    nome = input('Digite o Nome: ')
    idade = int(input('Informe a Idade: '))
    sexo = str(input('Informe o Sexo[M/F]: ')).strip().upper()
    # somaIdade = somaIdade + idade --->> somando a idade para depois dividir por 4
    idadeGrupo.append(idade) #adicionando as idades em uma lista
    media = (sum(idadeGrupo)) / 4 #somando os itens da lista e dividindo por 4
    if pessoa == 1 and sexo == 'M': # se a PESSOA for a 1 e o SEXO for M
        nomehomem = nome #nomeHomem recebe o nome
        idadeHomem = idade #idadeHomem recebe idade
    if sexo == 'M' and idade > idadeHomem: #se SEXO igual a M e a IDADE maior que idadeHomem
        idadeHomem = idade #substitui o valor reservado nas variáveis.
        nomehomem = nome
    if sexo == 'F': # se o SEXO igual A F
        if idade < 20: #compara a idade se é maior que 20
            contIdadeMulher +=1 # sendo maior, faz a contagem de cada ocorrência

print('-'*30)

print('A média de idade do grupo é {:.0f}'.format(media))
print('O Homem mais velho é {} com {} anos.'.format(nomehomem, idadeHomem))
print('Existem {} mulheres com menos de 20 anos.'.format(contIdadeMulher))


