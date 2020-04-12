print('=='*20)
print(' '*8,'10 TERMOS DE UMA PA')
print('=='*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro + (10-1)*razao
for c in range(primeiro, termo + razao, razao):
    print(' ',c, end='')
print(' Acabou!!!')