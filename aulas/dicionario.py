dicionario = {'curso':'Python para ML',
              'aluno':'Eduardo',
              'preco':'Gratuito',
              'nota':10 }

print(dicionario['aluno'])

#redefinindo valores
a = dicionario['nota'] = 8
print(a)

#criando novos valores
dicionario['Pré-requisito'] = 'Python básico'
print(dicionario)

#buscando todas as chaves do dicionario
print(dicionario.keys())

#buscando os valores das chaves

print(dicionario.values())

#mostrando tudo

print(dicionario.items())

#limpando o dicionario

print(dicionario.clear())


 