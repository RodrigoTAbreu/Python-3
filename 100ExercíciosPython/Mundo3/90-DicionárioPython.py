boletim = dict()
#solicitando a entrada de dados
boletim['nome'] = str(input('Digite o nome: '))
boletim['media'] = float(input('Digite a média: '))

#imprime os dados inseridos
print(f'O nome é igual a {boletim["nome"]}')
print(f'A média é igual a {boletim["media"]}')

#define a situação com base na média informada.
if boletim['media'] <= 5:
    print('A situação é igual a REPROVADO.')
elif 7 > boletim['media'] >=5.5:
    print('A situação é igual a RECUPERAÇÃO.')
else:
    print('A situação é igual a APROVADO.')

for k, v in boletim.items():
    print(f'{k} é igual a :{v}')
