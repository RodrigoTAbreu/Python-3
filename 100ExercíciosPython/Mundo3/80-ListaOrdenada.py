lista = []

while len(lista) <= 4:
    numero = int(input('Digite um numero: '))
    lista.append(numero)
    lista.sort()
print(lista)
print(len(lista))
