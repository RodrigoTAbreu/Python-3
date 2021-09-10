palavras = ('MERCADO','PYTHON','BOLA','AMANHECER','DIA')

for p in palavras:
    print(f'\nNa palavra {p} temos -> ',end='')#apresentadno a palavra
    for letra in p: # para cada letra in p(palavra) cada letra é uma lista
        if letra.lower() in 'aeiou':#dessa forma usamos o FOR
            print(letra, end=' ')

