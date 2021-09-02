respostas = {}
#define uma flag para indicar que a enquete está ativa

polling_active = True

while polling_active:
    #pede o nome da pessoa e a resposta
    name = input('\nQual é o seu nome? :')
    resposta = input('Qual montanha você gostaria de escalar algum dia? :')

    #armazena a resposta em um dicionário
    respostas[name] = resposta

    #descobre se outra pessoa vai responder a enquete
    repete = input('Gostaria de deixar outra pessoa responder?(yes/no):')
    if repete == 'no':
        polling_active = False
# a enquete foi concluida. Mostra os resultados
print('\n----Resultados da Enquete -----')
for name, resposta in respostas.items():
    print('{} gostaria de escalar a {}.'.format(name,resposta))