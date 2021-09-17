import urllib
import urllib.request

def validaacesso():
    '''
    Função Valida Acesso de um SITE.
    :param: site: solicita ao usuário a entrada de um endereço web
                da seguinte forma:
                <NomeDoSite>.<tipo COM, ORG, etc>.<Pais: BR, US,etc>
    '''
    site = str(input('Digite o Site:'))
    try:
        #site1=urllib.request.urlopen(f'https://www.{site}/')
        site2=urllib.request.urlopen(f'http://www.{site}/')
    except urllib.error.URLError:
        print('O Site não está acessível no momento.')
    else:
        print('Site acessível com SUCESSO.')


help(validaacesso)
validaacesso()