
totmil = maior = menor = cont = valorprod = total = 0
nomeprodmenor = nomeprodmaior = ' '
while True:
    nomeprod = str(input('Nome do Produto: '))
    valorprod = float (input('Valor do Produto: R$'))
    total += valorprod
    cont +=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]:')).upper().strip()[0]
    if valorprod >= 1000:
        totmil +=1
    if cont == 1:
        maior = menor = valorprod
        nomeprodmenor = nomeprodmaior = nomeprod
    else:
        if valorprod > maior:
            maior = valorprod
            nomeprodmaior = nomeprod
        if valorprod < menor:
            menor = valorprod
            nomeprodmenor = nomeprod


    if resp == 'N':
        print('fim')
        print('O maior valor é {} no valor de R${}'.format(nomeprodmaior, maior))
        print('E o menor valor é {} no valor de R${} '.format(nomeprodmenor, menor))
        print('Total da compra é R$ {} e {} produtos acima de R$1.000,00'.format(total, totmil))

        break