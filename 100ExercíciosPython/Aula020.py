def titulo(txt):
      print('---'*10)
      print(txt)
      print('---'*10)

titulo('Pensando em Python')

def soma(a,b):
      s = a + b
     print(s)

def contador(*num):
      for valor in num:
          print(f'{valor} ', end='')
          tam = len(num)
          print(f'O contador tem o tamanho {tam}')

def dobra(lst):
     posicao = 0
     while posicao <len(lst):
         lst[posicao] *=2
         posicao += 1

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Soma dos valores {valores} tem {s}')

# contador = [9,5,1]
# print('**'*30)
# dobra(contador)
# print(contador)

soma(5,2)
soma(2,9,4)