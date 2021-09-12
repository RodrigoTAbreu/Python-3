nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(nota1, nota2, media))

if 7 > media >= 5:
    print('Você está de RECUPERAÇÃO')
elif media >= 7:
    print('Você está de APROVADO')
elif media < 5:
    print('Você está REPROVADO.')

