def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f

def dobro(n):
    res = n*2
    return res

def triplo(n):
    res = n*3
    return res

def metade(n):
    res = n/2
    return res

def aumento(n,taxa):
    res = n+((n*taxa)/100)
    return res

def diminuir(n,taxa):
    return n-((n*taxa)/100)