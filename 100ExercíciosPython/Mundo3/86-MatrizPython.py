matriz = [[0,0,0],[0,0,0],[0,0,0]] # lista com as posições definidas
for l in range(0,3): # para linha de 0 a 3
    for c in range(0,3): # para a coluna de 0 a 3
# adiciona os valores na lista e nas posições já predefinidas LINHA E COLUNA
        matriz[l][c] = int(input(f'Digite o valor para [{l},{c}]: '))
print('=='*30)
# para cada linha de 0 a 3
for l in range(0,3):
    for c in range(0,3):#para cada coluna de 0 a 3
        print(f'[{matriz[l][c]:^5}]', end=' ') #imprime a lista na posição L e C
    print()