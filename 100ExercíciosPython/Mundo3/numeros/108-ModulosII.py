import numeros
num = int(input('Digite um número: '))
print(f'A metade de {numeros.moeda(num)} é {numeros.moeda(numeros.metade(num))}')
print(f'O dobro de {numeros.moeda(num)} é {numeros.moeda(numeros.dobro(num))}')
print(f'Com diminuir de -10% o valor é {numeros.moeda(numeros.diminuir(num,10))}')
print(f'Com aumento de 10% o valor é {numeros.moeda(numeros.aumento(num,10))}')
