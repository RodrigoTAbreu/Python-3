def ficha(jog='<desconhecido>', gol = 0):
    print(f'O Jogador{jog} fez {gol} gol(s) no campeonato.')

#programa principal
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: ')) #recebendo um numero porem com valor STRING
if g.isnumeric(): # vereficando se G pode ser um numero ou não
    g = int(g) #se for numeric o G recebe o int de G
else:
    g = 0 # se não G recebe o 0

if n.strip() == '': # vereficando se tirei todos os espaçoes e ainda assim ele ficou vazio
    ficha(gol = g) #se nome for vazio, ele vai passar apenas a qtd de G
else:
    ficha(n,g) # se não ele vai passar os dois parametros.
