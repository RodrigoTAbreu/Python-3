from datetime import date
ano = int(input('Informe o ano, para ano atual informe (0):'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano informado {} é Bisexto'.format(ano))
else:
    print('O ano informado {} não é Bisexto'.format(ano))