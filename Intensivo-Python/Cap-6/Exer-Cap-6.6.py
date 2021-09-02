linguagens = {'jean':'C#',
              'Roberto':'Ruby',
              'Carla':'HTML',
              'Ana':'C#',
              'Rodrigo':'Python',
              'Carlinha':'HTML'
    }
novos = ['Maria','Claudia','Bruno','Carla','Ana','Rodrigo']
for nome in novos:
    if nome in linguagens.keys():
        print('Obrigado por ter respondido {}'.format(nome))
    else:
        print('Não esqueça de participar da enquete {}'.format(nome))