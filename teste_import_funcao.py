import numpy
def calcPerimCir(raio):
    try:
        raio = float(raio)
    except:
        res = 'Valor do raio inválido'
    else:
        res = 2 * numpy.pi * raio
    return res