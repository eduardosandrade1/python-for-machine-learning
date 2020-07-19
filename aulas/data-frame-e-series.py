import pandas as pd 

alunos = {'Nome':['Eduardo','Pedro','Marcos', 'Carlos'],
          'Nota':[4, 7, 5.5, 9],
          'Aprovado':['Não', 'Sim','Não','Sim']
          }

dataframe = pd.DataFrame(alunos)

print(dataframe)

#series são unidimensional
objeto1 = pd.Series([1,4,6,5,2,3])
print(objeto1)