numeros = ('zero','um','dois','três','quatro',
           'cinco','seis','sete','oito','nove','dez')
continua = ' '

while True:# enquanto for verdade
    n = int(input('Digite um número: ')) # recebe o valor de N do usuário
    while n not in range(0,11): # enquanto N não está entre a RANGE(0,11)
        print('Digite um número de 0 a 10.') #imprime msg de alerta
        n = int(input('Digite um número: ')) #solicita o N novamente.

    print(f'Você digitou {n} {numeros[n]}.') #imprime o resultado N e a posição de N na tupla

    continua = input('Quer continuar[S/N]: ').upper()[0].strip() # solicita o continue para usuário

    if continua == 'N': #sendo negativo ele para o programa.
        break

print('fim')


