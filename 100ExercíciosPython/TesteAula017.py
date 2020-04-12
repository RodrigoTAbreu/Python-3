num = [2,5,9,1,7,8]
num[5]=6
if 3 in num:
    num.remove(3)
else:
    num.insert(4,35)

print(num)

valores = list(range(1,11))
print(valores)
valores.sort(reverse=True)
valores.remove(4)
print(valores)
print(f'Essa lista tem {len(valores)} itens')
if 4 in valores:
    valores.remove(4)
    print('Deseja continuar?')
else:
    print(f'O numero {4} não está na lista')
print('///'*20)

vlr = []
vlr.append(5)
vlr.append(9)
vlr.append(4)

for c, v in enumerate(vlr):
    print(f'Na posição {c} encontrei {v}!')
print('Cheguei ao final da lista.')

valor = list()
for cont in range(0,5):
    valor.append(int(input('Digite um valor: ')))

for pos, cont in enumerate(valor):
            print(f'Na posição {pos} encontrei o valor {cont}')
print('fim da lista')