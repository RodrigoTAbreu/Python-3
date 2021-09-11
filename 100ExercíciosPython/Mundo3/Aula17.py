lanche = ['Hamburguer','Pudim','Suco','Picole']
print(lanche)
lanche.insert(0,'Banana')
print(lanche)
lanche.remove('Suco') #remove pelo valor
print(lanche)
lanche.pop(2) #remove pela chave
print(lanche)

valores = list(range(1,15))# cria uma lista apartir de um range
print(valores)
valores.sort(reverse=True)#mostra a lista reversa
print(valores)
print(len(valores))#mostra o tamanho da lista
valores.append(0)
print(valores)
valores.pop()
print(valores)
valores.insert(2,1)
print(valores)
valores.remove(1)
print(valores)
vlr = []
vlr.append(9)
vlr.append(7)
vlr.append(5)
'''
for cont in range(0,5):
    vlr.append(int(input(f'Digite um valor: ')))

for c, v in enumerate(vlr):
    print(f'Na Chave {c} temos o valor {v}')
   '''
a = [2,3,4,7]
b = a[:] # B recebe uma cópia do valor A
print(a)
print(b)
b[2] = 10
print(b)