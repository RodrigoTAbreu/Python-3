ano = int(input('Informe o ano. '))
bisexto = ano %4
if bisexto == 0:
    print('O ano {} é bisexto.'.format(ano))
else:
    print('O ano {} não é bisexto.'.format(ano))