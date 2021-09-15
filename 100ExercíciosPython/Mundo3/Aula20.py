'''def mostraLinha(msg):
    print('-='*20)
    print(msg)
    print('-=' * 20)

def soma(a,b):
    s = a + b
    print(s)

mostraLinha(str(input('Qual sistema: ')))
soma(4,8)

def contador(*num): # asterisco significa desempacotar
    for valor in num:
        print(f'Os valores são {valor}')
    print(f'São {len(num)} numeros')

contador(2,8,4,9)
contador(2,1,3)
contador(4,8,9,3,4,8,23)'''

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores{valores} temos {s}')

soma(5,2)
soma(2,9,4)