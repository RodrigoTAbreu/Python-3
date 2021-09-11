
valores = []
#Criando a lista pela entrada do usuário até o tamanho de 0 a 5
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {cont}:')))

#quando o CONT for igual a 0, as variaveis MAIOR e MENOR recebem o valor
#de VALORES na posição CONT
    if cont == 0:
        maior = menor = valores[cont]
    else: #não sendo a primeiro valor de CONT
        if valores[cont]>maior: #verifica se o valor de VALORES[cont] é maior que MAIOR
            maior = valores[cont]
        if valores[cont]< menor:# ao contrário tb valida o menor valor
            menor = valores[cont]
print('**'*30)
print(f'Você digitou os valores {valores}.')
print(f'O maior valor é {maior} nas posições.',end='')

for i, valor in enumerate(valores): #buscando a chave e o valor na lista valores
    if valor == maior: # se valor encontrado for igual ao maior
        print(f'{i}..',end='') # imprime a chave da lista
print('')
print(f'O menor valor é {menor} nas posições.',end='')
for i, valor in enumerate(valores):
    if valor == menor:
        print(f'{i}..',end='')




