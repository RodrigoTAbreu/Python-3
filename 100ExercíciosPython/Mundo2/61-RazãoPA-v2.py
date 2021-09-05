numero = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
const = 1
pa = numero
while const <=10:
    pa += razao # não é necessário formula pois a PA é o primeirotermo mais a soma da razão
    print(' {} ->'.format(pa),end='')
    const += 1
print('FIM !!')