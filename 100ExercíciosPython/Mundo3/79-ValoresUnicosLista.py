lista = []
resp =' '
while True:#enquanto for verdade
    num = int(input('Digite um valor: '))# entrada de numeros pelo usuário
#se o NUM não está na lista
    if num not in lista:
        lista.append(num)#adiciona o numero na lista
    else:
        print('Valor já digitado.')

#pergunta ao usuário se deseja continuar
    resp = (input('Deseja continuar ? [S/N]:').upper()[0])
    if resp == 'N': #para o programa quando ele digitar N
        break
lista.sort()
print(lista)