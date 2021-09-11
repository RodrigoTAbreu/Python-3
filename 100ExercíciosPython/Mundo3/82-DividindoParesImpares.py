lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    resp = input('Quer continuar? [S/N]: ').upper()[0]
    if n%2==0:
        par.append(n)
    if n%2!=0:
        impar.append(n)

    if resp == 'N':
        break
print(f'Lista geral {lista}')
print(f'Lista números pares{par}')
print(f'Lista numero impar {impar}')