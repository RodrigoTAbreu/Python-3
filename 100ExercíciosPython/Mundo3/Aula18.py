'''teste = []
teste.append('Rodrigo')
teste.append(41)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

galera = [['João', 19], ['Ana', 33], ['Maria', 20]]
'''print(galera[2][0])'''

'''for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')'''

dado = []
'''for c in range(0,4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) #dado[:] faz uma cópia da lista dado
    dado.clear()'''

print(galera)
totalmaior = totalmenor = 0
for pessoa in galera:
    if pessoa[1] >=20:
        print(f'Pessoa {pessoa[0]} é maior de idade.')
        totalmaior +=1
    else:
        print(f'Pessoa {pessoa[0]} é menor de idade.')
        totalmenor +=1

print(f'Temos {totalmaior} maiores e {totalmenor} menores.')