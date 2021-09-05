primeiroTermo = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
const = 1
pa = primeiroTermo
qtdTermos = primeiroTermo

total = 0
mais = 10

while mais !=0:
    total =total + mais
    while const <= total:
        print(' {} -->'.format(pa), end='')
        pa += razao # não é necessário formula pois a PA é o primeirotermo mais a soma da razão
        const += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você quer mostrar?[0-para encerrar]: '))
print('Finalizado com {} termos apresentados'.format(total))