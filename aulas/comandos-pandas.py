import pandas as pd 

alunosDIC = {'Nome':['Eduardo','Pedro','Marcos', 'Carlos'],
          'Nota':[4, 7, 5.5, 9],
          'Aprovado':['Não', 'Sim','Não','Sim']
          }

alunosDF = pd.DataFrame(alunosDIC)

print(alunosDF.head())
#tamano do dataframe
print(alunosDF.shape)

#infos sobre as ver numericas, maior, menor, média
print(alunosDF.describe())