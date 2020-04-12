lista = list()
tempar = list()
temimpar = list()
temp = list()
for c in range(1,5):
    lista.append(int(input(f'Digite o {c}º valor:')))
    if lista[c] % 2 ==0:
        temp.insert(0,lista)
    else:
        temp.insert(1,lista)

print(f'Pares são {temp[0]}')
print(f'Ímpares são {temp[1]}')
'''for p in temp:
    if lista[0] % 2 == 0:
        #tempar.insert(0,)
        print(f'O Valores PARES foram {p}')
    if lista[1] %2 !=0:
        #temimpar.append(p)
        print(f'Os Valores Impares foram {p}')
lista.clear()
temimpar.sort()
tempar.sort()
#print(f'Os valores em Par são:{tempar}')
#print(f'Os valores em Impar são: {temimpar}')'''