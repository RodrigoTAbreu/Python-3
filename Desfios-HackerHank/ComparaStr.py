nomeA = input("Informe o Seu Nome: ")
nomeB = input("Informe Outro nome: ")
print('O Nome 1 é {} e o Nome 2 é {}'.format(nomeA, nomeB))
if 'celsius' in nomeA and nomeB:
    print('Você informou celsius')
else:
    print('O nome digitado foi {}'.format(nomeA or nomeB))