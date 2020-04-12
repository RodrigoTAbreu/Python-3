from datetime import date
nascimento = int(input('Informe o ano de nascimento: '))
ano = date.today().year
alistar = 18
resultado = nascimento - ano
if resultado >= 18:
    print('Você deve se alistar')
else:
    resultado < 18:
    print('Você ainda não precisa se alistar')
    elif nascimento - 18:\
        print('Ainda falta {} anos para você se alistar'.format(nascimento))