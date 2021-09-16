def notas(*n, sit = False):
    """
    --> Função para analisar situação de vários alunos.
    :param n: uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: retorna um dicionário com várias informações sobre a situação da turma.
    """
    result = dict()
    result['total'] = len(n)
    result['maior'] = max(n)
    result['menor'] = min(n)
    result['media'] = sum(n)/len(n)

    if sit:
        if result['media']>=7:
            result['situação'] = 'Boa'
        elif result['media'] >=5:
            result['situação'] = 'Razoável'
        else:
            result['situação'] = 'RUIM'

    return result


#PGR principal
resp = notas(5.5,1,2.5,sit=True)
print(resp)
help(notas)

