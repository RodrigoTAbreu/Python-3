print('=='*20)
print('Calculando a média de um aluno')
print('=='*20)

n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2 # não esquecer de usar a ordem de precedência
print('A média do aluno foi {:.3}.'.format(media))