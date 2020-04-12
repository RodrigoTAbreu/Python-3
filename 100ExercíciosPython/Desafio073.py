times = ('Flamengo', 'Santos', 'Palmeiras', 'Gremio', 'Atletico-PR',
         'São Paulo', 'Internacional', 'Corinthians','Fortaleza', 'Goias')
print('=='*60)
print('Os cinco primeiros colocados foram \n',times[:5])
print('=='*60)
print('Os últimos foram \n',times[-4:])
print('=='*60)
print('Ordem alfabetica:\n ',sorted(times))
print('=='*60)
print(f'O São Paulo ficou na {times.index("São Paulo")+1}ª posição')


