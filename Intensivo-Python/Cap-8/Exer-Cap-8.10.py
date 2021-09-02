magicos = ['josé','pedro','guilherme','antonio']
magic = []
def show_magicos(magicos):
    for magico in magicos:
        print('\t {}'.format(magico))

def make_great(magicos):
    for magico in magicos:
        magicos.append('O grande '+magico)

make_great(magicos)
show_magicos(magicos)