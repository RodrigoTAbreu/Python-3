distancia = float(input('Qual é a distancia da viagem? KM'))
passagem = 0.50 * distancia
passagem2 = 0.45 * distancia
if distancia >200:
    print('O total da passagem é R$ {:.2f}.'.format(passagem2))
elif distancia <200:
    print('O total da viagem é R$ {:.2f}.'.format(passagem))
