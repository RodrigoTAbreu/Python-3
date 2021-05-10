linguagens = {'jean':'C#',
              'Roberto':'Ruby',
              'Carla':'HTML',
              'Ana':'C#',
              'Rodrigo':'Python',
              'Carlinha':'HTML'
              }
print('Essas são as linguagens de nossa equipe. ')
for linguagen in linguagens.values(): #.values pega o valor de cada cabeçalho
    print(linguagen.title())

print('=='*20)
print('Aplicando FOR IN SET')
print('=='*20)
print('Aplicando o conjunto SET')
for linguagen in set(linguagens.values()):
    print(linguagen.title())