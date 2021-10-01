n = int(input('Digite o Valor: '))

for i in range(1,n):
    if n % 5 == 0 and n % 3 == 0:
        print('fizz-buzz')
    elif n % 3 == 0:
        print('fizz')
    elif n % 5 == 0:
        print('buzz')
    else:
        print(n)
print('Fim')
