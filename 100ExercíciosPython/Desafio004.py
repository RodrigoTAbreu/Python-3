t = input('Digite algo: ')
print('Tipo primitivo desse valor é:', type(t))
print('Só tem espaços?',t.isspace())
print('É um número? ', t.isnumeric())
print('É alfabetico?', t.isalpha())
print('É alfanumerico?', t.isalpha())
print('Está em maiusculas?', t.isupper())
print('Está em minusculas?{}'.format(t.islower()))
print('Está capitalizado?{}'.format(t.istitle()))

