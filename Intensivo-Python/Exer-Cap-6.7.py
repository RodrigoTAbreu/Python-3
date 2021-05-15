mora_fora = {
    'primeiro_nome':'caio',
    'ultimo_nome':'silva',
    'idade':'34',
    'cidade':'london',

            }
mora_brasil = {
    'primeiro_nome':'maria',
    'ultimo_nome':'santos',
    'idade':'30',
    'cidade':'brasil'
                }
viaja_muito = {
    'primeiro_nome':'bruna',
    'ultimo_nome':'costa',
    'idade':'20',
    'cidade':'viaja muito'
            }
pessoas = []
pessoas.append(mora_brasil)
pessoas.append(viaja_muito)
pessoas.append(mora_fora)

for nome in pessoas:
    print('{}'.format(nome['primeiro_nome'].title()))
    print('\tidade:{}'.format(nome['idade'].title()))
    print('\tCidade:{} '.format(nome['cidade'].title()))
    print('Lista original com todos os dados é \n\t{}'.format(pessoas))