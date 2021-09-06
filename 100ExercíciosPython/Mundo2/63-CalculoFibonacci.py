n = int(input('Informe um número: ')) #recebendo o número
t1 = 0 # primeiro termo
t2 = 1 # segundo termo
print('-->> {} -->> {}'.format(t1, t2),end='') #impressão dos termos
cont = 3 #contador iniciando em 3
while cont<=n: # enquanto contador for menor que N da entrada
    t3 = t1 + t2 # termo 3 soma o primeiro e o segundo termo
    print(' -->> {}'.format(t3),end='')
    t1 = t2 # termo 1 passa ser o t2
    t2 = t3 # termo 2 passa ser o t3
    cont +=1 # contador soma +1
print(' -->> FIM.')