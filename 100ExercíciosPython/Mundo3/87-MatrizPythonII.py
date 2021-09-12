matriz = [[0,0,0],[0,0,0],[0,0,0]]
result = par1 = par2 = impar = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para [{l},{c}]: '))

        if c % 2 ==0:
            par1 += c
        if l % 2 == 0:
            par2 += l
result = par1 + par2
print(f'Valor total de PARES é: {result}')
print(f'PAR 1 {par1}')
print(f'PAR 2 {par2}')
print(type(matriz))




#print('=='*30)
#for l in range(0,3):
#    for c in range(0,3):
#        print(f'[{matriz[l][c]:^5}]', end=' ')
#    print()