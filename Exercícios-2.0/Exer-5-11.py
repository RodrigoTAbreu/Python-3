numeros = [1,2,3,4,5,6,7,8,9]
for numeros in numeros:
    if numeros == 1:
        print('{}st'.format(numeros))
    elif numeros == 2:
        print('{}nd'.format(numeros))
    elif numeros == 3:
        print('{}rd'.format(numeros))
    else:
        print('{}th'.format(numeros))