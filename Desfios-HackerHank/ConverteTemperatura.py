temperatura = float(input('Informe a temperatura: '))
escalaOrigem =input('Informe a Escala de Origem: ')
escalaDesejada =input('Informe a Escala Desejada: ')

def converteTemperatura(temperatura, escalaOrigem, escalaDesejada):
    result = float
    kelvin = 273.15
    origem = ['celsius', 'kelvin', 'fahrenheit']
    desejada = ['celsius','kelvin','fahrenheit']
    if escalaOrigem.strip() in origem and escalaDesejada.strip() in desejada:
        if escalaOrigem.strip() == 'celsius':
            if escalaDesejada.strip() == 'kelvin':
                result = float(temperatura + kelvin)
                print('{:.2f}'.format(result))
            elif escalaDesejada.strip() == 'fahrenheit':
                result = float(temperatura*1.8)+32
                print('{:.2f}'.format(result))
        elif escalaOrigem.strip() == 'kelvin':
            if escalaDesejada.strip() == 'celsius':
                result = float(temperatura - kelvin)
                print('{:.2f}'.format(result))
            elif escalaDesejada.strip() == 'fahrenheit':
                result = float(temperatura - kelvin)*9/5+32
                print('{:.2f}'.format(result))
        elif escalaOrigem.strip() == 'fahrenheit':
            if escalaDesejada.strip() == 'celsius':
                result = float(temperatura-32)*5/9
                print('{:.2f}'.format(result))
            elif escalaDesejada.strip() == 'kelvin':
                result = float(temperatura - 32)*5/9+kelvin
                print('{:.2f}'.format(result))
        else:
            print("Informe um valor Válido (celsius / kelvin / fahrenheit")
    else:
        print("O informe um valor de temperatura válido.")
    print(result)

converteTemperatura(temperatura, escalaOrigem, escalaDesejada)

