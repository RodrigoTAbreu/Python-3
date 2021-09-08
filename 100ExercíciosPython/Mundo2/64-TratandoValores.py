n = 0
digitados = []
while n != 999:
    digitados.append(n)
    n = int(input('Digite um valor:'))
    resultado = sum(digitados)
digitados.pop(-1)
print('Você digitou {} e a soma total é {}'.format(len(digitados),resultado))
