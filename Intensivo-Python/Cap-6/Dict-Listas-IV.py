usuarios = {
    'aeinstein': {
        'primeiro': 'albert',
        'segundo' : 'einstein',
        'lugar': 'pricenton'
    } ,
    'mcurie':{
        'primeiro': 'marie',
        'segundo' : 'curie',
        'lugar': 'paris'
    }
}

for nome_usuario, info_usuario in usuarios.items():
    print('\n{}'.format(nome_usuario))
    nome_completo = info_usuario['primeiro'] + ' ' + info_usuario['segundo']
    lugar = info_usuario['lugar']
    print('\tNome completo: {}'.format(nome_completo.title()))
    print('\tLugar: {}'.format(lugar.title()))