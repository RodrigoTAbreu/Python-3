#começa com alguns design que devem ser impressos
unprinted_models = ['iphone case','robot pendant','dodecahedron']
completed_models = []
def print_models(unprinted_models,completed_models):
    #simula a impressão de cada desing, até que não haja mais nenhum
    #transfere cada desing para completed_models após impresso

    while unprinted_models:
        desing_atual = unprinted_models.pop()
        #simula a criação de uma impressão 3d a partir do desing
        print('Imprimindo Modelo: {}'.format(desing_atual))
        completed_models.append(desing_atual)

def show_completed_models(completed_models):
    #Exibe todos os modelos finalizados.
    print('\nOs seguintes modelos foram impressos:')
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_models, completed_models)
show_completed_models(completed_models)