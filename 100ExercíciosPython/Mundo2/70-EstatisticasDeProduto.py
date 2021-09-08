totCompra = maisCaro = maisBarato = 0
nomeProdBarato = nomeProdCaro =  str
while True:
    produto = input('Digite o nome do produto: ')
    valor = float(input('Qual o valor do produto:R$ '))
    continua =' '
    totCompra += valor
    while continua not in 'SN':
        continua = input('Continua [S/N]:').upper()[0]

    if maisCaro < valor:
        maisCaro = valor
        nomeProdCaro = produto

    if continua == 'N':
        break
print(f'Total das Compras {totCompra}')
print(f'Produto mais Caro custa R${maisCaro} e é {nomeProdCaro}')

