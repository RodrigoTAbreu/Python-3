cont = 0
n = (int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')),
     int(input('Digite um valor: ')), int(input('Digite um valor: ')),)


print(f'O numero 3 aparece na posição {n.index(3)+1}')
print(f'O numero 9 apareceu {n.count(9)} vez.')

for c in n:
    if c%2==0:
        cont +=1
print(f'São ao todo {cont} numeros pares')


