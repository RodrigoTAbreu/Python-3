from datetime import date
anoNasc = int(input('Informe o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc

if idade < 9:
    print('Sua idade é {}'.format(idade))
    print('Sua equipe é a MIRIM.')
elif 14 > idade >= 9:
    print('Sua idade é {}'.format(idade))
    print('Sua equipe é a INFANTIL.')
elif 19 > idade >=14:
    print( 'Sua idade é {}'.format( idade ) )
    print('Sua equipe é a JUNIOR.')
elif 25 > idade >=19:
    print( 'Sua idade é {}'.format( idade ) )
    print('Sua equipe é a SENIOR.')
elif idade >=25:
    print( 'Sua idade é {}'.format( idade ) )
    print('Sua equipe é a MASTER. ')