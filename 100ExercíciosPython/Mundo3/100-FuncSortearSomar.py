from random import randint
num = list()
listaPar = list()
def sorteia():
    contador = 0
    while contador < 5:
        c = randint(0,5)
        num.append(c)
        print(f'Valor sorteado foi {c}')
        contador +=1
        if c%2==0:
            listaPar.append(c)


def soma(listaPar):
    print(f'A soma dos números PARES sorteados é: {sum(listaPar)}')
    print(f'A soma de todos os números sorteados {sum(num)}')


sorteia()
print(f'Valores sorteados foram {num}')
soma(listaPar)