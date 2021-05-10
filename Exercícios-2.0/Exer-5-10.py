usuarios_cadastrados = ['Maria','Tania','Pedro','José', 'Antonio','admin','ISA']
usuarios_novos = ['Ana','Clara','TANIA','Taty','Isa']
novos = []
cadastrados = []

for usuarios_cadastrados in usuarios_cadastrados:
    cadastrados.append(usuarios_cadastrados.upper())

for usuarios_novos in usuarios_novos:
    novos.append(usuarios_novos.upper())

for novos in novos:

    if novos in cadastrados:
        print('Usuário {} já existe !!!'.format(novos))
    else:
        print('Disponível')
