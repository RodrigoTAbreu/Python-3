velo = float(input('Qual a velocidade do Carro: '))
rápido = 80
if velo > rápido:
    vmulta = velo - rápido
    multa = vmulta * 7
    print('Você foi multado, e a sua multa será de {}'.format(multa))
else:
    print('Continue a viagem')