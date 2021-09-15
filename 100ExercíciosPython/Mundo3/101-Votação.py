
s = 0
def voto(ano):
    from datetime import date # importa a biblioteca DATETIME
    anoAtual = date.today().year # pega o ano do computador.
    s = anoAtual-ano # soma a idade
    #Faz a validação de idades
    if 60 > s >=18:
        print(f'Com {s} anos, Voto Obrigatório.')
    elif s <= 17:
        print(f'Com {s} anos, Voto NEGADO')
    elif s >= 61:
        print(f'Com {s} anos, voto OPCIONAL')

#Programa Principal solicitando a entrada do ano para usuário.
voto(int(input('Digite o Ano de Nascimento: ')))

