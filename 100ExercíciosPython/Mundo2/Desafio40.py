nota1 = int(input('Informe a Primeira Nota:'))
nota2 = int(input('Informe a Segunda Nota:'))
nota3 = int(input('Informe a Terceira Nota:'))

media = (nota1+nota2+nota3)/3
print('Sua média foi de {:.1f} Você está:'.format(media))
if media >7:
    print('--->Aprovado')
elif media == 7:
    print('--->Recuperação')
elif media < 7:
    print('--->Reprovado')