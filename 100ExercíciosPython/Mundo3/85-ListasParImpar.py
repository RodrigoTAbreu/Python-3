lista = [[],[]]
n = 0

for c in range(1,8):
    n = int(input(f'Digite o {c}° um número: '))
    if n %2==0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print(f'Os pares são {lista[0]}.')
print(f'Os ímpares são {lista[1]}.')