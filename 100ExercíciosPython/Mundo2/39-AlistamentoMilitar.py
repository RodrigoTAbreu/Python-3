from datetime import date

atual = date.today().year
ano = int(input('Qual é seu ano de nascimento ? '))
idade = atual - ano
sexo = input('Qual é o Sexo?:[M/F]')

if sexo.lower()== 'f':
    print('O alistamento é apenas para Homens.')
elif sexo.lower() == 'm':
    if idade == 18:
        print('Você tem {} anos e precisa se alistar'.format(idade))
    elif idade < 18:
        maior = 18 - idade
        print('Você tem {} anos, você vai se alistar em {}'.format(idade,(maior + atual)))
    elif idade > 18:
        alistado = (atual - idade)+18
        print('Você tem {} anos.'.format(idade))
        print('Você já deveria ter se alistado em {}'.format(alistado))
else:
    print('Digite um valor válido: [M/F]')
