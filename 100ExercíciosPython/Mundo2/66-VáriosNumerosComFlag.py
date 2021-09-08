n =s= c = 0
while True:
    n = int(input('Digte um Número [999 finaliza]:'))
    if n == 999:
        break
    s += n
    c +=1
print(f'A soma dos numeros é {s}. Total de nº digitados foi {c}')