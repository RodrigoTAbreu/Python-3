def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def dobro(n = 0):
    res = n*2
    return res

def triplo(n = 0):
    res = n*3
    return res

def metade(n = 0):
    res = n/2
    return res

def aumento(n = 0,taxa = 0):
    res = n+((n*taxa)/100)
    return res

def diminuir(n = 0,taxa = 0):
    return n-((n*taxa)/100)

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')
