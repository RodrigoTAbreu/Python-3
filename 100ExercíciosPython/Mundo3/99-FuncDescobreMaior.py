def maior(* num):#função maior() - *(asterisco) indica que serão receber vários parametros e será desenpacotados.
    print('Valores sendo analisados...')
    for valor in num: #para cada valor em num
        print(f' {valor}.',end='' )
    print(f'São {len(num)} ao todo.') #confirmando a qtd de num ou o tamanho
    if num == 0:
        num = 0
        print('O valor informado é Zero')
    print(f'O maior entre eles é {max(num)}') #max encontra o maior valor
    print('-='*20)

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
