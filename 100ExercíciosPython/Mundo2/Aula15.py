n = c =s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    c +=1
    s += n

#print('A soma é {}'.format(s))
print(f'A soma é {s:-^20}') #python 3.6+ com FString
print(f'Qtd de numeros digitados foram {c}')