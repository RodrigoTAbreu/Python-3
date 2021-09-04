from datetime import date
contMaior = 0
contMenor = 0
pessoa = 0
for c in range(0,7):# iniciando a range até o 7
    pessoa +=1 #iniciando o contador de vezes a ser inserido
    ano = int(input('Em que ano a {} nasceu?: '.format(pessoa))) # solicita a entrada de ano da pessoa
    maior = date.today().year - ano #pega o ano atual do computador e calcula MENOS o ano informado.
    if maior >= 18: # sendo MAIOR igual ou maior que 18
        contMaior += 1 # soma contadorMaior
    else:
        contMenor += 1 #ou soma contadorMenor
print('{} pessoas são maiores de idade.'.format(contMaior))
print('{} pessoas não menores de idade'.format(contMenor))
