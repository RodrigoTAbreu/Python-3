pessoas = {'nome':'rodrigo','sexo' : 'M','Idade':22}
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos.')
print()
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():# mostra a chave
    print(k)
for k,v in pessoas.items(): #mostra chave e valor
    print(f'{k} = {v}')

'''del pessoas['sexo'] #apaga a chave em específico
print(pessoas)
''''''
pessoas['nome'] = 'Leandro' # altera o valor contido na chame NOME
print(pessoas)
pessoas['peso'] = 98 #adiciona ao dicionario a chave PESO com o valor 98
print(pessoas)
'''

estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil = []

brasil.append(estado1)
brasil.append(estado2) #adiciona o dicionário em uma lista
print(brasil)
print(brasil[0]) #imprime o valor contido na posição 0 da lista
print(brasil[1])

print(brasil[1]['uf'])#imprime da lista BRASIL na posição 1 o valor da chave UF

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
