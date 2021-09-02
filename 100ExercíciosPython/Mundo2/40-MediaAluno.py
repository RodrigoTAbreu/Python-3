nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota:'))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Você ficou com media {:0.1f}. REPROVADO'.format(media))
elif media <6.9 and media >5.0:
    print('Você ficou com média {:0.1f}. RECUPERAÇÃO'.format(media))
elif media >= 7.0:
    print('Você ficou com {:0.1f}. APROVADO'.format(media))