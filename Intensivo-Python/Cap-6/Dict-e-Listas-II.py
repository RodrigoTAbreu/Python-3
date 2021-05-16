linguagens_favoritas = {
    'João' : ['python','ruby'],
    'sara' : ['c'],
    'eduardo': ['ruby','go'],
    'phil' : ['python','haskell']
}

for nome, linguagens in linguagens_favoritas.items():
    print("{}'s'. Suas linguagens favoritas são: ".format(nome))
    for linguagem in linguagens:
        print('\t{}'.format(linguagem))

# 1º for >> para cada nome e linguens IN dicionario
# linguagens_favoritas.items() ( pegando seus itens individuais
# imprime o nome de cada participante
# 2º for >> para cada linguagem IN linguagens ( este ultimo gerado
# pelo for anterior.
# imprime o nome dos itens que estão na lista de cada nome.