def somaQuadrados(a,b):
    somaQ = a**2 + b **2
    return somaQ

print(somaQuadrados(2,3))

#funcao lambda com parametros a se receber
somaQuadrados2 = lambda a,b: a**2 + b**2
print(somaQuadrados2(2,3))

#lambda sem atributos a se receber
mostraNome = lambda: print('Olá mundo!')
mostraNome()