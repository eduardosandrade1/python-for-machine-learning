import pandas as pd 
dados = pd.read_excel('/home/martilian/Desktop/machine-learning-python/arquivos/Livro1.xlsx')

print(dados.head())

teste = pd.read_csv('/home/martilian/Desktop/machine-learning-python/arquivos/athlete_events.csv')
teste.head()