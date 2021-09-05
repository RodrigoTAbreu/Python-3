sexo = str(input('Informe o sexo: ')).upper().strip()[0] # com [0] ele pega somente a primeira letra
cont = 0
#outra forma do WHILE
# while sexo not in 'MmFf':
while sexo != 'M' and sexo !='F':
    sexo = str(input('Dados inválidos. Informe seu Sexo[M/F]:')).upper().strip()[0]
    cont +=1
print('Foram necessárias {} tentativas.'.format(cont))
