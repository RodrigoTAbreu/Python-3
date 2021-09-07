from random import randint
n = c = 0
while True:
    n = int(input('Qual nº você quer saber a tabuada?:'))
    if n <0:
        break
    for c in range(1,11):
        print(f'{n} X {c} = {n*c:3}')
    c=0
print('Você finalizou')