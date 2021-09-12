s = 0
contador = 0
for c in range(1,501, 2): #iniciando a contagem de 1 até 501  pulando de 2 em 2 dessa forma ele mostra os impares
    if c % 3 == 0: # SE contador for divisivel por 3 sendo seu resultado igual a zero
        s = s + c # somando os valores encontrados em C podemos simplificar da seguinte forma S+= C
        contador = contador + 1  # contando quantas vezes ele achou c ( ou contador += 1)
print('A soma de todos os {} valores solicitados é {}'.format(contador,s)) # imprime contador
print('FIM')
