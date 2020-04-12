

def voto(nasc):
    from datetime import datetime # ao importar dentro de uma DEF ela sera usada apenas quando a DEF for invocada
    now = datetime.now()
    ano = now.year
    idade = ano - nasc
    if idade < 16:
        return f' Com {idade} anos, NÃO VOTA.'
    elif idade >= 16 and idade <= 60:
        return f' Com {idade} anos, voto OBRIGATORIO.'
    elif idade >= 60:
        return f' Com {idade} anos, voto Opcional'

print(voto(int(input('Informe o ano de nascimento: '))))