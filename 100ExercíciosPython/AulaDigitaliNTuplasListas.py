lista = [1,0,23,34,5,9]
animal = ['gato', 'cachorro', 'elefante']
nova = animal * 3 #triplicando lista
print(nova)
print(animal[0])
print(type(lista))
soma = 0

for x in lista:
    print(animal)
    soma+= x
print(soma)

print(sum(lista)) # funciona apenas para dados do mesmo tipo (numero)

print(max(lista))
print(min(lista))
print((min(animal))) # neste caso ele segue a sequencia do alfabeto.

if 'lobo' in animal:
    print('Tem gato na lista')
else:
    print('Não existe')
    animal.append('lobo')
    print('Animal incluso')
    print(animal)

animal.pop(1)
print(animal)
print(lista)
#lista.remove(2)
#print(lista)
