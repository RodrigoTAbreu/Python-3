from time import sleep
from datetime import date
resp = ' '
idade = 0
sexoh = 0
sexom = 0
idadem = 0
print('-='*20)
print(' '*10,'Informe DADOS')
print('-='*20)
while True:
   if resp == 'N':
       print('Fim')
       break
   else:
        sexo = str( input( 'Informe o Sexo [M/F]:' ) ).upper().strip()[0]
        idade = int( input( 'Informe a Idade: ' ) )
        resp = str( input( 'Deseja Continuar [S/N]?: ') ).upper().strip()[0]
        if sexo =='M':
            sexoh += 1
        if sexo == 'F' and idade >20:
            sexom += 1
            idadem += 1
        elif sexo == 'F':
            sexom +=1
    #if sexo != 'FfMm':
   # print('Entrada errada, informe F ou M')
print('Processando Informações', end='')
sleep(1)
print('...')
print('*'*70)
print(f'Foram informados {sexoh} Homens e {sexom} Mulheres sendo {idadem} maiores de 20anos')
print('*'*70)
print('Informações processadas em:')