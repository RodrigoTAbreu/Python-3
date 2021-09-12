s = 0
cont = 0

for c in range(1,7): # iniciando contagem de 1 a 7
    n = int(input('Iforme o {}º valor: '.format(c))) # solicitando ao usuário a entrada de um numero, isso irá se repetir 7 vezes
    if n %2 ==0: # se o numero informado for PAR ele executa as contas abaixo
        s += n #S soma ele mesmo mais o N informado pelo usuário
        cont += 1 #CONT soma ele mesmo mais 1
print('Você informou {} numero(s) par(es) e a soma deles é {}'.format(cont,s))

print('Fim!!!')
