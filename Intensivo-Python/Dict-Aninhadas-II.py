#Criar uma lista vazia para armazenar alienígenas
aliens =[]
#Cria 30 alienígenas verdes
for alien_number in range(30):
    novo_alien = {'color':'green','pontos':5,'velocidade':'slow'}
    aliens.append(novo_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['velocidade'] = 'medium'
        alien['pontos'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['velocidade'] = 'fast'
        alien['pontos'] = 15

#mostra os 5 primeiros alienígenas
for alien in aliens[:30]:
    print(alien)
print('...')
#mostra quantos alienígenas foram criados
print('Total de alienígenas é {}'.format(len(aliens)))