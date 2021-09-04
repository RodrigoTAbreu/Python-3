pesoMenor = 0
pesoMaior = 0
for c in range(1,6):
    peso = float(input('Informe o peso da {} pessoa: '.format(c)))
    if c == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        elif peso < pesoMenor:
            pesoMenor = peso
print('O peso maior lido foi {}'.format(pesoMaior))
print('O peso Menor lido foi {}'.format(pesoMenor))
