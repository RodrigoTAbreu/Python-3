import datetime
idade = int(input('Informe a idade:'))


if idade == 18:
    print('Necessário alistamento Militar.')
elif idade < 18:
    print('Ainda não é necessário alistamento.')
elif idade > 18:
    print('Você já deveria ter se alistado.')

