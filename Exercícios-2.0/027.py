n = str(input('Digite o Nome: ')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu sobrenome é {}'.format(nome[len(nome)-1]))
