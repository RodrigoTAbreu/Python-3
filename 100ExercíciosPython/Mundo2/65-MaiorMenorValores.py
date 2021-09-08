n = soma = media =cont = resp = 0
numeros = []
while resp != 'N':
    n = int(input('Digite um número: '))
    numeros.append(n)
    resp = str(input('Quer continuar [S/N]:')).strip().upper()[0]
    cont +=1
    soma = sum(numeros)
    media = float(soma / cont)
print('A Soma é {}'.format(soma))
print('A Média é {:.2f}'.format(media))
print('O Menor valor é {} e o Maior é {}.'.format(min(numeros),max(numeros)))