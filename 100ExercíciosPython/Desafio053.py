frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junta = ''.join(palavras)
inverso = ''

for letra in range(len(junta)-1, -1, -1):
    inverso += junta[letra]
print('O inverso de {} é {}'.format(junta, inverso))
if junta == inverso:
    print('É Palindromo')
else:
    print('Não é Palindromo')
