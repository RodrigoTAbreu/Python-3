listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Caneta', 22.30,
            'Livro', 34.90)

for posicao in range(0, len(listagem)): #para cada posição no RANGE de 0 até o tamanho da LISTAGEM
    if posicao % 2 == 0:                #se a posição for par ou seja a segunda
        print(f'{listagem[posicao]:.<30}',end='') # o alinhamento da listagem na posição será completada com 30 espaços
                                                # e alinhados a esquerda (:< )
    else:
        print(f'R${listagem[posicao]:>7.2f}')   #sendo a posição impar o alinhamento ocorrerá a direita (:>) sendo completos com
                                                # duas casas decimais (.2f)
print('**'*40)