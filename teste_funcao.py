userIn = input('Introduza um numero:')

def dataFunction(numero):
    try:
        num_conv = float(numero)
    except:
        resultado = 'Valor Inválido'
    else:
        if num_conv > 3:
            resultado = 'Numero maior que 3'
        elif num_conv < 3:
            resultado = 'Numero menor que 3'
        else:
            resultado = 'Numero igual a 3'
    
    return resultado

res = dataFunction(userIn)
print(res)