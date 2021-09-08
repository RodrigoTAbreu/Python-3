print('-='*20)
print('{:^35}'.format('Caixa Eletronico.'))
print('-='*20)
vlrSaque = int(input('Qual valor Deseja Sacar: R$ ')) #entrada do valor a sacar
total = vlrSaque #Total recebe o valor que irá ser sacado
cedula = 50 #CÉDULA recebe 50 que é a maior nota do sistema
totCedulas = 0 #receberá a qdt de células
while True: # faça enquanto for verdade.
    if total >=cedula: #se o TOTAL (que é o valor de saque) for maior ou igual a CÉDULA ( que é 50)
        total -= cedula #total diminui ele (total ) pela variavel cédula
        totCedulas += 1 #total das somas de cédulas recebe o valor de mais 1
    else: #se não
        if totCedulas >0:# se o Total de Cédulas for maior que zero
            print(f'Total de {totCedulas} cédulas de R$ {cedula}') #imprime a frase
        if cedula == 50: #se cedula for igual a 50
            cedula = 20 #cedula recebe um novo valor que é 20
        elif cedula == 20: #senão se cedula for igual a 20
            cedula = 10 #cedula recebe 10
        elif cedula == 10:#senão se cedula for igual a 10
            cedula = 1 #cedula recebe 1
        #sai do laço IF
        totCedulas = 0 #total de cédulas recebe 0
        if total ==0: # se o total for igual a 0
            break# para o programa
