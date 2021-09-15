#help(len) #doc string
#from time import sleep

#def contador(i,f,p):
'''
   # -> Faz uma contagem e mostra na tela.
   # i = inicio
   # f = final
   # p = passo
   # Função criada por Rodrigo durante o curso de Python
    '''
 #   for c in range(i,f,p):
  #      sleep(1)
   #     print(f' {c}',end='')

#contador(0,100,10)
#help(contador)

#def soma(a,b,c = 0):# essa identificação de ZERO significa que C recebe 0 caso não seja informado
'''
    Soma de valores.
    a = primeiro valor
    b = segundo valor
    c = terceiro valor, padrão é 0.
    '''
#    s = a + b + c
#    print(f'A soma dos valores é {s}')


#help(soma)
#soma(3,2)

'''def teste():
    global n #indicamos global dizendo para o Python q n será usado dentro e fora da função com o mesmo valor
    x = 8
    print(f'Na função n vale {n}')
    print(f'Na função X vale {x}')

n = 2
print(f'No pgr principal n vale {n}')

teste()
'''
def soma(a = 0 , b = 0, c = 0):
    s = a+b+c
    return s # retorna um resultado mais não imprime


# formas de como imprimir com o uso do return.
r1 = soma(3,2,5)
r2 = soma(1,7)
r3 = soma(6)
print(f'Meu calculos deram {r1}, {r2} e {r3}')
print('Ou')
print(f'O o resultado é: {soma(3, 2, 5)}')
print(f'O o resultado é: {soma(1,7)}')
print(f'O o resultado é: {soma(6)}')
