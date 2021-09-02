magicos = ['josé','pedro','guilherme','antonio']

def show_magicos(magicos):
    for magico in magicos:
        print('\tApresentamos o mágico {}'.format(magico))

def make_great(magicos):
    for magico in magicos:
        print('O grande {}'.format(magico))


print(magicos)
make_great(magicos)