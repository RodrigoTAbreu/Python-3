import numeros
num = int(input('Digite um número: '))
print(f'A metade de {numeros.moeda(num)} é {numeros.metade(num,False)}')
print(f'O dobro de {numeros.moeda(num)} é {numeros.dobro(num,True)}')
print(f'Com diminuir de -10% o valor é {numeros.diminuir(num,10,True)}')
print(f'Com aumento de 10% o valor é {numeros.aumento(num,10,True)}')
