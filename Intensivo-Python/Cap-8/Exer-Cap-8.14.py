def carro(fabricante, marca, **dados):
    '''Armazena dados sobre um carro'''
    info_carro = {}
    info_carro['Fabricante'] = fabricante
    info_carro['Marca'] = marca
    for key, value in dados.items():
        info_carro[key] = value
    return info_carro
dados_carro = carro('subaru','outback',cor = 'blue', opcionais = 'AR-Quente')

print(dados_carro)