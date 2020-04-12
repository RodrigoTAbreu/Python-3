lista = list()

cont = 0
while True:
    resp = ' '
    n = int(input('Digite o Valor: '))
    if n not in lista:
        lista.append(n)
        print('Um novo valor foi inserido')
    else:
        print('Valor já existe')


    while resp not in 'SN':
        resp = str(input('Deseja Continuar? [S/N]:')).strip().upper()[0]
    if resp =='N':
        break
lista.sort()
print(lista)
