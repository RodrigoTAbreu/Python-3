cidade = str(input('Qual nome da Cidade:')).strip()  ## .strip remove os espaços##
existe = 'SANTO' in cidade
print('O nome digitado é ', existe) #aqui analisa apenas em maiusculo
print('Você nasceu em uma cidade da região: ', cidade[:5] == 'SANTO') # aqui analisa apenas em maiusculo
print(cidade[:5].upper() == 'SANTO') ## aqui estamos convertendo tudo para maiusculo e analisando em maiusculo
