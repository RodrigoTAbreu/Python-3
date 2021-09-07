n = c = 0
numeros = []
while True:
    n = int(input('Digte um Número [999 finaliza]:'))
    if n == 999:
        break
    numeros.append(n)
    soma = sum(numeros)
    c +=1
print(f'A soma dos numeros é {soma}. Total de nº digitados foi {c}')