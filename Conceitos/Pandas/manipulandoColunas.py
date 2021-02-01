import pandas as pd

dados = pd.read_csv('C:/Users/CASSIO/Documents/Python/Aprendendo-python/Conceitos/pandas/athlete_events.csv')

dados.rename(columns={'Name':'Nome', 'Age':'Idade', 'Height':'Altura', 'Weight':'Peso'}, inplace=True)
print(dados.head())
print('-'*30)

medalhas = dados['Medal'].value_counts()
print(medalhas)
print('-'*30)

genero = dados['Sex'].value_counts()
print(genero)
print('-'*30)

analise = dados.describe()
print(analise)