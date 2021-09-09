lanche = ('Hamburguer','Suco','Pizza','Pudim')
print(lanche)

for comida in lanche:
    print(f'Comendo {comida}')
print('**'*20)


for comida in range(0,len(lanche)):
    print(f'Comendo com RANGE agora {lanche[comida]} na posição {comida}')
print('**'*20)

for posicao, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {posicao}')
print('**'*20)
print(lanche)
print(sorted(lanche))
print('**'*20)
a = (2,5,4,)
b = (5,8,1,2)
c = a+ b
print(c)
print(len(c))
print(c.count(5))
print(c.index(1,4))
del(c)
