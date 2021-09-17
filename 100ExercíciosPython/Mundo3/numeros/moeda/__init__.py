def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def dobro(n = 0, formato=False):
    res = n*2
    return res if not formato else moeda(res)

def triplo(n = 0, formato=False):
    res = n*3
    return res if not formato else moeda(res)

def metade(n = 0, formato=False):
    res = n/2
    return res if formato is False else moeda(res)

def aumento(n = 0,taxa = 0, formato=False):
    res = n+((n*taxa)/100)
    return res if formato is False else moeda(res)

def diminuir(n = 0,taxa = 0, formato=False):
    res = n-((n*taxa)/100)
    return res if formato is False else moeda(res)

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:>.2f}'.replace('.',',')

def resumo(preco= 0, taxaA=10, taxaR=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(preco)}')
    print(f'Dobro do Preço: \t{dobro(preco,True)}')
    print(f'Metade do Preço: \t{metade(preco,True)}')
    print(f'{taxaA}% de Aumento: \t{aumento(preco,taxaA,True)}')
    print(f'{taxaR}% de Redução: \t{diminuir(preco,taxaR, True)}')

    print('-'*30)