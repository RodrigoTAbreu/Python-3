def formatando_nomes(primeiro_nome, segundo_nome):
    nome_completo = '{} {}'.format(primeiro_nome, segundo_nome)
    return nome_completo.title()

#Este é o loop infinito
while True:
    print('\nInforme seu nome coompleto. ')
    print('Pressione [q] para sair a qualquer momento.')
    f_nome = input('Primeiro Nome: ')
    if f_nome == 'q':
        break
    l_nome = input('Último nome: ')
    if l_nome == 'q':
        break
    nome_formatado = formatando_nomes(f_nome,l_nome)
    print('Olá {}, seja bem vindo(a).'.format(nome_formatado))
