lista = (
'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
'PROGRAMADOR', 'FUTURO')
for p in lista:                                         #para cada posição na lista
    print(f'\nNa palavra {p.upper()} temos:', end='')   #imprime a posição em maiuscula {p.upper()}
    for letra in p:                                     #para cada letra em P (posição)
        if letra.lower() in 'aeiou':                    #se a letra está (ou é) em 'aeiou'
            print(letra, end=' ')                       #imprime a letra

