lista = par = impar = listaT = list()
n = 0

while True:
    n = int(input('Digite o Valor: '))
    resp = ' '
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    if n % 2 !=0:
        impar.append(n)
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break

listaT = par + impar + lista
print(f'LISTAS JUNTAS {listaT}')
print(f'PAR{par}')
print(f'IMPAR {impar}')
print(f'LISTA {lista}')