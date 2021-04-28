import random
print('='*25)
print('Escolhendo Aluno')
print('='*25)
nome = ['Maria','Joao', 'Julia', 'José']
res = random.choice(nome)
print('O escolhido dessa vez foi {}.'.format(res))
