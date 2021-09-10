times = ('São Paulo','Palmeiras','Timeco','Santos',
         'Bragantino','Santo André','Atletico MG','Atletico PR',
         'Cruzeiro', 'Vila Nova','Fortaleza','Bahia',
         'Recife','Flamengo','Fluminense','Botafogo',
         'América MG','Inter-RS','Gremio')
print('**'*20)
print(f'Os Cinco primeiros são {times[0:5]}') #os quatro primeiros
print('**'*20)
print(f'Os quatro últimos são {times[-5:]}') #cinco ultimos
print('**'*20)
print(f'Times por ordem alfabética {sorted(times)}')
print('**'*20)
print(f'O Vila Nova está na {times.index("Vila Nova")+1}ª posição') #Procurando a posição de um item

'''print('O Vila Nova está na posição: ',end='') #outra maneira de buscar a posição do time
print((times.index('Vila Nova')+1),'º')'''
print('**'*20)

print('--'*30)
print(' '*15,end='')
print('Tabela Completa')
print('--'*30)

for pos, time in enumerate(times):
    print(f'O time {times[pos]} está na posição {pos}')

print('fim')