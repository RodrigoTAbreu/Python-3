'''fruta = str(input('Informe a Fruta ')).upper()
while not fruta=='MAÇÃ': #quando se tornar falso ENQUANTO NÃO FOR MAÇÃ
    print('Passo')
    print('Pula')
    fruta = str(input('Informe a Fruta: ')).upper()
'''
'''
c = 1 # definindo a variável inicial
while c<10: #enquanto o C for menor que 10
    print(c)
    c +=1
'''
'''
c = 1 # iniciando a variável em 1
r = 'S'
numeros = [] # criando a lista que vai acumular os valores digitados
while r == 'S': #enquanto C for diferente de 0
    numeros.append(c) # adiciona o valor de C na lista
    c = int(input('Informe o valor: ')) # solicita nova entrada
    r = str(input('Quer continuar? ')).upper()
print('Numeros digitados foram {}'.format(numeros)) # no fim imprime os valores.
'''
n = 1
par = impar = 0
while n != 0: #enquanto N for diferente de 0
    n = int(input('Digite um valor: ')) # solicita a entrada de novo valor
    if n !=0: # s o N for diferente de 0
        if n % 2 == 0: # se o resto da divisão por 2 for igua a 0
            par +=1
        else:
            impar +=1
print('Foram digitados {} numeros pares e {} ímpares.'.format(par, impar))
