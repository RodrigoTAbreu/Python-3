print('-='*20)
print(' '*10, 'NUMEROS PRIMOS')
print('-='*20)
n = int(input('Informe um número: '))       #solicitando um numero ao usuário
t = 0                                       # criando uma variavel de contagem iniciando em 0 (zero)
for c in range(1,n+1):                      #contador inicia em 1 e vai até o numero informado pelo usuário + 1 que é para ele mostrar o ultimo numero
    if n % c == 0:                          #se o numero informado DIVIDIDO pelo contador for IGUAL a ZERO
        print('\033[33m', end=' ')          #ele imprime colorido, final da linha com espaço mantendo o contador na mesma linha
        t += 1                              #variavel contagem recebe mais um valor a cada passagem do contador até seu fim
    else:
        print('\033[31m', end=' ')          #se não ele imprime o contador de outra cor
    print('{}'.format(c), end=' ')          # ao fim do laço imprime o contador na mesma linha
print('\n\033[mO número {} foi divisível {} vezes'.format(n, t))# terminado o laço ele vai imprimir a mensagem 'O numero foi divisivel tantas vezes
if t == 2:                                  #vereficando se ele é primo basta considerar quantas vezes ele foi divisível
    print('Portanto {} É PRIMO.'.format(n)) #, sendo duas ele é primo
else:                                       #caso contrário não é primo
    print('Portanto {} NÃO É PRIMO.'.format(n))