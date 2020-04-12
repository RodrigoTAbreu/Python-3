def maior(* num):
    print('Valores sendo analisados...')
    for valor in num:
        print(f' {valor}.',end='' )
    print(f'São {len(num)} ao todo.')
    if num == 0:
        num = 0
        print('O valor informado é Zero')
    print(f'O maior entre eles é {max(num)}')
    print('-='*20)

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
