n = int(input('Digite um número: '))
for c in range(0, 11): # contador de 0 a 10
    r = n * c  #usando acumulador para multiplicar o numero inserido pelo contador
    print('{} X {:2} = {}'.format(n,c, r)) # essa foi a forma de print que utilizei
    print('{} x {:2} = {}'.format(n,c,n*c)) # esse foi o print da monstrado na aula, veja que ele calcula n*c dentro de format e o resultado em print.
print('Fim!!!!')
