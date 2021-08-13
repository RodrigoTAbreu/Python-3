ano = int(input('Informe o ano de nascimento:'))
idade = 2021 - ano
print('Idade é {}'.format(idade))
print('sua categoria é :')
if idade < 9:
    print('Mirim')
elif idade <14: #or idade >=9:
    print("infantil")
elif idade <19 : #or idade >=14:
    print('Junior')
elif idade <20 : #or idade >= 19:
    print('Senior')
elif idade >=21:
    print('Master')
