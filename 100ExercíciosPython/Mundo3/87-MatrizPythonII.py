matriz = [[0,0,0],[0,0,0],[0,0,0]]
result = par1 = par2 = impar =scol =  0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para [{l},{c}]: '))

        if c % 2 ==0:
            par1 += c
        if l % 2 == 0:
            par2 += l
result = par1 + par2
print(f'Valor total de PARES é: {result}')

for l in range(0,3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')

for c in range(0,3):
    if c == 0:
        mai = matriz[l][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')





#print('=='*30)
#for l in range(0,3):
#    for c in range(0,3):
#        print(f'[{matriz[l][c]:^5}]', end=' ')
#    print()