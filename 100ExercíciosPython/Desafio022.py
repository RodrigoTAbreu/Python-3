nome = str(input('Digite seu nome:')).strip()
print('Nome em maiusculas: {}'.format(nome.upper()))
print('Nome em minusculas: {}'.format(nome.lower()))
print('Seu nome tem ao todo: {}'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))

