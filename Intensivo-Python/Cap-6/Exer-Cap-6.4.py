glossario = {
    'STR':'Tipo de dado String',
    'IF':'Tipo de Laço de Repetição',
    'Boolean':'Dado Booleano(True/False)',
    'Input':'Entrada de usuário',
    'Sum':'Soma valores alocados em variáveis'
}

glossario['FOR In Set'] = 'Procura valores únicos no dicionario'
glossario['.values()'] = 'Apresenta os valores de cada chave'
glossario['sorted()'] = 'Coloca em ordem os itens do dicionário'
glossario['if..Not..in'] = 'Instrução que busca o que NÃO ESTÁ'
glossario['.keys()'] = 'Apresenta as chaves dentro de um dicionário'

for item in glossario.keys():
    print('Esses termo é importante {}'.format(item))
    #print('Termos encontrados: {}'.format(item.title()))

