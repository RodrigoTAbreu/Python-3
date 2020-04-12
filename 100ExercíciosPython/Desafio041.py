from datetime import date
print('='*42)
print('*'*10,'\033[1;33;41mCATEGORIA DE ATLETAS\033[m','*'*10)
print('='*42)
nasc = int(input('Digite o ano de Nascimento: '))
print('='*30)
anoatual = date.today().year
idade = anoatual - nasc


print(''' Averiguando a categoria:
Até 9 anos - MIRIM.
Até 14 anos - INFANTIL
Até 19 anos - JUNIOR
Até 20 anos - SÊNIOR
Acima de 21 anos - MASTER''' )
print('='*30)

print('O Atleta nasceu em {} e sua idade é {} anos. Portanto sua categoria é:'.format(nasc, idade))
if idade >= 21:
    print('\033[7mMASTER\033[m')
elif 20 >= idade > 19:
    print('\033[7mSÊNIOR\033[m')
elif 19>= idade > 14:
    print('\033[7mJUNIOR\033[m')
elif 14>= idade >9:
    print('\033[7mINFANTIL\033[m')
elif 9 >= idade:
    print('\033[7mMIRIM\033[m')