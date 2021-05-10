idade = int(input('Qual a idade? :'))
if idade < 2:
    print('Você ainda é um BEBÊ.')
elif idade< 4:
    print('Você ainda é uma criança.')
elif idade < 13:
    print('Você é um(a) garoto(a).')
elif idade < 20:
    print('Você é um adolescente.')
elif idade  <65 :
    print('Você é um adulto(a).')
elif idade > 65 :
    print('Você é idoso.')
