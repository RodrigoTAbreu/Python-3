sexo = str(input('Informe o sexo: ')).upper()
cont = 0
while sexo != 'M' and sexo !='F':
    sexo = str(input('Dados inválidos. Informe seu Sexo[M/F]:')).upper()
    cont +=1
print('Foram necessárias {} tentativas.'.format(cont))
