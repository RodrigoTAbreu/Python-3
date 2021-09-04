frase = str(input('Digite a frase:')).strip().upper() #.strip() elimina os espaços / .upper() coloca tudo em maiusculas
palavras = frase.split() #quebrando a frase palavra a palavra
junto = ''.join(palavras)# juntando as palavras sem espaço
inverso = ''
inverso = junto[::-1] # pode-se utilizar esse macete de fatiamento, dessa forma elimina o FOR
'''for letra in range(len(junto)-1, -1, -1): #para cada letra na range do TAMANHO de JUNTO até o final(-1), até a ultima letra (-1), contando de regressivo (-1)
    inverso += junto[letra] #somando a variavel inverso a variavel JUNTO na posição LETRA
'''
if inverso == junto: # verificando se ambas são iguais
    print('É um palíndromo!!')
else:
    print('Não é palindoromo.')

print(junto, inverso)