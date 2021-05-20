local = {}
incluir = True

while incluir:
    nome = input('qual seu nome? :')
    local_escolhido = input('Qual local de suas próximas férias? :')
    local[nome] = local_escolhido
    repetir = input('Gostaria de incluir outro na enquete?(Yes/No):')
    if repetir == 'no':
        incluir = False

print('Resultados da Enquete')
for nome, local_escolhido in local.items():
    print('{} vai passar as férias em {}'.format(nome, local_escolhido))
