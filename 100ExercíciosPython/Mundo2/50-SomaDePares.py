result =0
contador = 0
# solcitando a leitura de diversos numeros ao usuário.
for c in range(1,7):
    n = int(input('Digite um valor: '))
#Identificando se o numero digitado é par.
    if n %2 == 0:
        #inicando a contagem  e a soma dos pares encontrados.
        result = result + n
        contador = contador+1

print('A soma dos pares é {}'.format(result))
print('Foram encontrados {} números pares.'.format(contador))
